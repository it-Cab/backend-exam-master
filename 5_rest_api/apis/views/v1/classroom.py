from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from apis.models import Classroom, Teacher, Student
from apis.serializers import ClassroomSerializer


class ClassroomListView(generics.ListAPIView):
    """
    API สำหรับดึงรายการห้องเรียนทั้งหมด
    สามารถกรองห้องเรียนตามโรงเรียนได้
    """

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["school"]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        for classroom in response.data:
            classroom_obj = Classroom.objects.get(id=classroom["id"])
            classroom["school"] = classroom_obj.school.name  # เปลี่ยน school เป็นชื่อโรงเรียน
        return response


class ClassroomCreateView(generics.CreateAPIView):
    """
    API สำหรับสร้างห้องเรียนใหม่
    """

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class ClassroomRetrieveView(generics.RetrieveAPIView):
    """
    API สำหรับดูรายละเอียดของห้องเรียน พร้อมรายชื่อครูและนักเรียน
    """

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    def retrieve(self, request, *args, **kwargs):
        classroom = get_object_or_404(Classroom, pk=kwargs["pk"])
        data = ClassroomSerializer(classroom).data
        data["school"] = classroom.school.name

        # ดึงข้อมูลครูที่สอนในห้องนี้
        teachers = Teacher.objects.filter(classrooms=classroom)
        data["teachers"] = [{"id": teacher.id, "first_name": teacher.first_name, "last_name": teacher.last_name} for teacher in teachers]

        # ดึงข้อมูลนักเรียนในห้องนี้
        students = Student.objects.filter(classroom=classroom)
        data["students"] = [{"id": student.id, "first_name": student.first_name, "last_name": student.last_name} for student in students]

        return Response(data, status=status.HTTP_200_OK)


class ClassroomUpdateView(generics.UpdateAPIView):
    """
    API สำหรับอัปเดตข้อมูลห้องเรียน
    """

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class ClassroomDeleteView(generics.DestroyAPIView):
    """
    API สำหรับลบห้องเรียน
    """

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
