from django.urls import path
from . import views
from .views import about, StudentProfile, StudentSubjectList, view_attendance, MarkList, TeacherProfile,\
    TeacherSubjectList, mark_attendance, add_marks,DepartmentList, DepartmentView, contact

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('department_list/', DepartmentList.as_view(), name='dep_list'),
    path('department_view/<int:pk>/', DepartmentView.as_view(), name='dep_view'),
    path('contact/', views.contact, name='contact'),
    path('stu_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('stu_profile/', StudentProfile.as_view(), name='student_profile'),
    path('student_subject-list/', StudentSubjectList.as_view(), name='student_subject_list'),
    path('stu_attendance/', view_attendance, name='student_attendance'),
    path('stu_mark_list/', MarkList.as_view(), name='student_mark_list'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher_profile/', TeacherProfile.as_view(), name='teacher_profile'),
    path('teacher_subject-list/', TeacherSubjectList.as_view(), name='teacher_subject_list'),
    path('mark_attendance/', mark_attendance, name='mark_attendance'),
    path('add-marks/', add_marks, name='add-marks')
]