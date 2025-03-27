from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import get_object_or_404
from apis.models import Teacher
from apis.serializers import TeacherSerializer



class TeacherListView(generics.ListAPIView):
    """
    API สำหรับดึงรายการคุณครูทั้งหมด
    สามารถกรองคุณครูตามโรงเรียน, ห้องเรียน, ชื่อ, และเพศได้
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "classrooms__school",
        "classrooms",
        "first_name",
        "last_name",
        "gender",
    ]
    search_fields = ["first_name", "last_name"]


class TeacherCreateView(generics.CreateAPIView):
    """
    API สำหรับสร้างคุณครูใหม่
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherRetrieveView(generics.RetrieveAPIView):
    """
    API สำหรับดูรายละเอียดของคุณครู พร้อมข้อมูลห้องเรียน
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def retrieve(self, request, *args, **kwargs):
        teacher = get_object_or_404(Teacher, pk=kwargs["pk"])
        data = TeacherSerializer(teacher).data

        # ดึงข้อมูลห้องเรียนของคุณครู
        data["classrooms"] = [
            {
                "id": classroom.id,
                "grade": classroom.grade,
                "section": classroom.section,
                "school": classroom.school.name,
            }
            for classroom in teacher.classrooms.all()
        ]

        return Response(data, status=status.HTTP_200_OK)


class TeacherUpdateView(generics.UpdateAPIView):
    """
    API สำหรับอัปเดตข้อมูลคุณครู
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDeleteView(generics.DestroyAPIView):
    """
    API สำหรับลบคุณครู
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer