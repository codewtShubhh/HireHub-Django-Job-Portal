from django.db import models
from companies.models import Companies


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Job(models.Model):
    JOB_TYPE = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
        ('contract', 'Contract'),
        ('remote', 'Remote'),
    )

    company = models.ForeignKey(
        Companies,
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='jobs'
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary_min = models.PositiveIntegerField(blank=True, null=True)
    salary_max = models.PositiveIntegerField(blank=True, null=True)
    experience = models.PositiveIntegerField(default=0, help_text='Minimum years of experience required')
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    skills = models.TextField(help_text='Comma-separated skills')
    deadline = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company.company_name}"