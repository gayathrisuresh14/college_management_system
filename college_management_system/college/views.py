from django.shortcuts import render, redirect
from .models import Student, Subject, Attendance, Mark, Teacher, Department, Contact
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import MarkAttendanceForm, MarkSubmissionForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contacts = Contact(name=name, email=email, message=message)
        contacts.save()

    return render(request, 'contact.html')


class DepartmentList(ListView):
    model = Department
    context_object_name = 'dep_list'
    template_name = 'dep_list.html'

class DepartmentView(DetailView):
    model = Department
    context_object_name = 'department'
    template_name = 'dep_view.html'

@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    context = {
        'student': student
    }
    return render(request, 'student/stu_dashboard.html', context)


class StudentProfile(LoginRequiredMixin, View):
    template_name = 'student/stu_profile.html'

    def get(self, request, *args, **kwargs):
        student = Student.objects.get(user=request.user)
        return render(request, self.template_name, {'student': student})



class StudentSubjectList(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'student/sub_list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        student = Student.objects.get(user=self.request.user)
        return Subject.objects.filter(department=student.department)


@login_required
def view_attendance(request):
    student = Student.objects.get(user=request.user)
    subjects = Subject.objects.filter(department=student.department)

    attendance_data = []
    for subject in subjects:
        attendance_records = Attendance.objects.filter(student=student, subject=subject)
        total_classes = attendance_records.count()
        classes_attended = attendance_records.filter(status='P').count()
        if total_classes > 0:
            attendance_percentage = (classes_attended / total_classes) * 100
        else:
            attendance_percentage = 0

        attendance_data.append({
            'subject': subject,
            'total_classes': total_classes,
            'classes_attended': classes_attended,
            'attendance_percentage': attendance_percentage
        })

    context = {
        'attendance_data': attendance_data
    }

    return render(request, 'student/attendance.html', context)


class MarkList(LoginRequiredMixin, ListView):
    model = Mark
    template_name = 'student/marklist.html'
    context_object_name = 'mark_list'

    def get_queryset(self):
        student = self.request.user.student
        return Mark.objects.filter(student=student)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mark_list = context['mark_list']

        total_marks_obtained = sum(mark.marks_obtained for mark in mark_list)
        total_marks = sum(mark.total_marks for mark in mark_list)

        if total_marks > 0:
            percentage = (total_marks_obtained / total_marks) * 100

        else:
            percentage = 0

        context['percentage'] = percentage
        return context


# Teacher


@login_required
def teacher_dashboard(request):
    teacher = Teacher.objects.get(user=request.user)
    context = {
        'teacher': teacher
    }
    return render(request, 'teacher/teacher_dashboard.html', context)


class TeacherProfile(LoginRequiredMixin, View):
    template_name = 'teacher/teacher_profile.html'

    def get(self, request, *args, **kwargs):
        teacher = Teacher.objects.get(user=request.user)
        return render(request, self.template_name, {'teacher': teacher})


class TeacherSubjectList(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'teacher/teacher_sub.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        teacher = Teacher.objects.get(user=self.request.user)
        return Subject.objects.filter(teacher=teacher)



@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = MarkAttendanceForm(request.POST)
        if form.is_valid():
            form.save(teacher=request.user.teacher)
            form.save()
            return redirect('mark_attendance')
    else:
        form = MarkAttendanceForm
    return render(request, 'teacher/mark_attendance.html', {'form': form})


@login_required
def add_marks(request):
    if request.method == 'POST':
        form = MarkSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_dashboard')  # Redirect to teacher dashboard after successful submission
    else:
        form = MarkSubmissionForm()

    subjects = Subject.objects.filter(teacher=request.user.teacher)  # Filter subjects by logged-in teacher
    context = {
        'form': form,
        'subjects': subjects,
    }

    return render(request, 'teacher/add_marks.html', context)



