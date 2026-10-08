from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):

    USER_TYPE = (
        ('job_seeker','Job Seeker'),
        ('recruiter','Recruiter'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=30)
    skills = models.TextField()
    experience = models.PositiveIntegerField(default=0)
    resume =models.FileField(upload_to='resumes/',blank=True,null=True)
    profile_picture = models.ImageField(upload_to='Profile_picture/',blank=True,null=True)
    user_type = models.CharField(max_length=20,choices=USER_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username


