from rest_framework import generics, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apis.models import School, Classroom, Teacher, Student
from apis.serializers import SchoolSerializer


class SchoolListView(generics.ListAPIView):
    """
    API สำหรับดึงรายการโรงเรียนทั้งหมด
    สามารถกรองโรงเรียนตามชื่อได้
    """

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class SchoolCreateView(generics.CreateAPIView):
    """
    API สำหรับสร้างโรงเรียนใหม่
    """

    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolRetrieveView(generics.RetrieveAPIView):
    """
    API สำหรับดูรายละเอียดของโรงเรียน พร้อมนับจำนวนห้องเรียน, ครู, และนักเรียน
    """

    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def retrieve(self, request, *args, **kwargs):
        school = get_object_or_404(School, pk=kwargs["pk"])
        data = SchoolSerializer(school).data

        # นับจำนวนห้องเรียน, ครู, และนักเรียน
        data["classroom_count"] = Classroom.objects.filter(school=school).count()
        data["teacher_count"] = (
            Teacher.objects.filter(classrooms__school=school).distinct().count()
        )
        data["student_count"] = Student.objects.filter(classroom__school=school).count()

        return Response(data, status=status.HTTP_200_OK)


class SchoolUpdateView(generics.UpdateAPIView):
    """
    API สำหรับอัปเดตข้อมูลโรงเรียน
    """

    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolDeleteView(generics.DestroyAPIView):
    """
    API สำหรับลบโรงเรียน
    """

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
