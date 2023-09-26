from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.


def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        form.error_messages = {'invalid_login': 'Invalid credentials.'}  # Set custom error message
        if form.is_valid():
            user = form.get_user()
            if user.is_active:
                if user.is_staff:
                    messages.error(request, 'Invalid credentials.')
                    print('Invalid credentials for student login.')
                else:
                    login(request, user)
                    return redirect('student_dashboard')  # Redirect to student dashboard
    else:
        form = AuthenticationForm(request)
    return render(request, 'authentication/student_login.html', {'form': form})


def teacher_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        form.error_messages = {'invalid_login': 'Invalid credentials.'}
        if form.is_valid():
            user = form.get_user()
            if user.is_active:
                if not user.is_staff:
                    messages.error(request, 'Invalid credentials.')
                else:
                    login(request, user)
                    return redirect('teacher_dashboard')  # Redirect to teacher dashboard

    else:
        form = AuthenticationForm(request)
    return render(request, 'authentication/teacher_login.html', {'form': form})
