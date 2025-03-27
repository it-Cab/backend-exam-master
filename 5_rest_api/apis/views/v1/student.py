from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import get_object_or_404
from apis.models import Student, Classroom
from apis.serializers import StudentSerializer


class StudentListView(generics.ListAPIView):
    """
    API สำหรับดึงรายการนักเรียนทั้งหมด
    สามารถกรองนักเรียนตามโรงเรียน, ห้องเรียน, ชื่อ, และเพศได้
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "classroom__school",
        "classroom",
        "first_name",
        "last_name",
        "gender",
    ]
    search_fields = ["first_name", "last_name"]


class StudentCreateView(generics.CreateAPIView):
    """
    API สำหรับสร้างนักเรียนใหม่
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveView(generics.RetrieveAPIView):
    """
    API สำหรับดูรายละเอียดของนักเรียน พร้อมข้อมูลห้องเรียน
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def retrieve(self, request, *args, **kwargs):
        student = get_object_or_404(Student, pk=kwargs["pk"])
        data = StudentSerializer(student).data

        # ดึงข้อมูลห้องเรียนของนักเรียน
        classroom = student.classroom
        data["classroom"] = {
            "id": classroom.id,
            "grade": classroom.grade,
            "section": classroom.section,
            "school": classroom.school.name,
        }

        return Response(data, status=status.HTTP_200_OK)


class StudentUpdateView(generics.UpdateAPIView):
    """
    API สำหรับอัปเดตข้อมูลนักเรียน
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDeleteView(generics.DestroyAPIView):
    """
    API สำหรับลบนักเรียน
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
