from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    dep_id = models.CharField(max_length=10)
    description = models.TextField()
    dep_image = models.URLField(max_length=2083, default='None')

    def __str__(self):
        return self.dep_id


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    phone_num = models.CharField(max_length=10)
    gender = models.CharField(max_length=50)
    guardian = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    admission_date = models.DateField()
    profile_pic = models.URLField(max_length=2083)

    def __str__(self):
        return f"{self.name}- {self.department}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_num = models.CharField(max_length=10)
    gender = models.CharField(max_length=50, default='Unknown')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}- {self.department}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    sub_id = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sub_id}- {self.teacher}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.subject}"


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_date = models.DateField()
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.PositiveIntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name