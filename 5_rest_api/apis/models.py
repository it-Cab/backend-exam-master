from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name


class Classroom(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="classrooms"
    )
    grade = models.IntegerField()
    section = models.IntegerField()

    def __str__(self):
        return f"Grade {self.grade}/{self.section} - {self.school.name}"


class Teacher(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    classrooms = models.ManyToManyField(Classroom, related_name="teachers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name="students"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.classroom})"
