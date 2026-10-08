from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Companies(models.Model):

    recruiter = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='Companies'
    )

    company_name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='Company_Logo/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

