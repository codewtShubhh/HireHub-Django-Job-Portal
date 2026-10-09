from rest_framework import generics, permissions
from jobs.models import Job, Category
from applications.models import Application
from .serializers import JobSerializer, CategorySerializer, ApplicationSerializer
from django.contrib.auth.models import User
from.serializers import RegisterSerializer

from .permissions import IsJobSeeker, IsRecruiter



class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class JobListAPIView(generics.ListAPIView):
    queryset = (
        Job.objects.filter(is_active=True)
        .select_related('company','category')
        .order_by('-created_at')
    )        
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['location','job_type', 'category', 'experience']
    search_fields = ['title', 'description', 'skills']
    ordering_fields = ['created_at', 'salary_max']


class JobDetailAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.filter(is_active=True).select_related('company', 'category')
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class MyApplicationsAPIView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsJobSeeker()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        return (Application.objects.filter(applicant=self.request.user)
                .select_related('job', 'job__company'))

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
    