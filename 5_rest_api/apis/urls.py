from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views.v1.school import (
    SchoolListView,
    SchoolCreateView,
    SchoolRetrieveView,
    SchoolUpdateView,
    SchoolDeleteView,
)
from apis.views.v1.student import (
    StudentListView,
    StudentCreateView,
    StudentRetrieveView,
    StudentUpdateView,
    StudentDeleteView,
)
from apis.views.v1.classroom import (
    ClassroomListView,
    ClassroomCreateView,
    ClassroomRetrieveView,
    ClassroomUpdateView,
    ClassroomDeleteView
)
from apis.views.v1.teacher import (
    TeacherListView,
    TeacherRetrieveView,
    TeacherCreateView,
    TeacherUpdateView,
    TeacherDeleteView
)


urlpatterns = [
    path("schools/", SchoolListView.as_view(), name="school-list"),
    path("schools/<int:pk>/", SchoolRetrieveView.as_view(), name="school-detail"),
    path("schools/create/", SchoolCreateView.as_view(), name="school-create"),
    path("schools/update/<int:pk>/", SchoolUpdateView.as_view(), name="school-update"),
    path("schools/delete/<int:pk>/", SchoolDeleteView.as_view(), name="school-delete"),

    path("students/", StudentListView.as_view(), name="student-list"),
    path("students/create/", StudentCreateView.as_view(), name="student-create"),
    path("students/<int:pk>/", StudentRetrieveView.as_view(), name="student-detail"),
    path("students/update/<int:pk>/", StudentUpdateView.as_view(), name="student-update"),
    path("students/delete/<int:pk>/", StudentDeleteView.as_view(), name="student-delete"),

    path("classrooms/", ClassroomListView.as_view(), name="classroom-list"),
    path("classrooms/<int:pk>/", ClassroomRetrieveView.as_view(), name="classroom-detail"),
    path("classrooms/create/", ClassroomCreateView.as_view(), name="classroom-create"),
    path("classrooms/update/<int:pk>/", ClassroomUpdateView.as_view(), name="classroom-update"),
    path("classrooms/delete/<int:pk>/", ClassroomDeleteView.as_view(), name="classroom-delete"),

    path("teachers/", TeacherListView.as_view(), name="teacher-list"),
    path("teachers/create/", TeacherCreateView.as_view(), name="teacher-create"),
    path("teachers/<int:pk>/", TeacherRetrieveView.as_view(), name="teacher-detail"),
    path("teachers/update/<int:pk>/", TeacherUpdateView.as_view(), name="teacher-update"),
    path("teachers/delete/<int:pk>/", TeacherDeleteView.as_view(), name="teacher-delete"),

]

# from apis.views.v1.classroom import ClassroomViewSet

# router = DefaultRouter()
# router.register(r"classrooms", ClassroomViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]