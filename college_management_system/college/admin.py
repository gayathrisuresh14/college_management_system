from django.contrib import admin
from .models import Department, Student, Teacher, Subject, Attendance, Mark, Contact

# Register your models here.

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Mark)
admin.site.register(Contact)