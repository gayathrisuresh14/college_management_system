from django import forms
from .models import Attendance, Mark


class MarkAttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('student', 'subject', 'date', 'status')

    def save(self, commit=True, teacher=None):
        instance = super().save(commit=False)
        if teacher:
            instance.teacher = teacher
        else:
            instance.save()
        return instance


class MarkSubmissionForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['student', 'subject', 'exam_date', 'marks_obtained', 'total_marks']



