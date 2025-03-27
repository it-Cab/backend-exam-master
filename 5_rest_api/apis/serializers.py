from rest_framework import serializers
from .models import School, Classroom, Teacher, Student


class SchoolSerializer(serializers.ModelSerializer):
    classroom_count = serializers.IntegerField(
        source="classrooms.count", read_only=True
    )
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    def get_teacher_count(self, obj):
        return Teacher.objects.filter(classrooms__school=obj).distinct().count()

    def get_student_count(self, obj):
        return Student.objects.filter(classroom__school=obj).count()

    class Meta:
        model = School
        fields = "__all__"


class ClassroomSerializer(serializers.ModelSerializer):
    teachers = serializers.StringRelatedField(many=True, read_only=True)
    students = serializers.StringRelatedField(many=True, read_only=True)
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(), required=False
    )

    class Meta:
        model = Classroom
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    classrooms = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all(), many=True)
    school_names = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = "__all__"

    def get_school_names(self, obj):
        school_names = [classroom.school.name for classroom in obj.classrooms.all()]
        return set(school_names)


class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())

    class Meta:
        model = Student
        fields = "__all__"
