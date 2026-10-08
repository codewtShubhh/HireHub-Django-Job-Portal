from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'category',
            'title',
            'description',
            'location',
            'salary_min',
            'salary_max',
            'experience',
            'job_type',
            'skills',
            'deadline',
            'is_active',
        ]
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }