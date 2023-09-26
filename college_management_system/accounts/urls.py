from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('student-login/', views.student_login, name='student_login'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('logout/', LogoutView.as_view(), name='logout')
]