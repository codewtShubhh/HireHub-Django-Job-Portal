from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobListAPIView.as_view(), name='api_job_list'),
    path('jobs/<int:pk>/', views.JobDetailAPIView.as_view(), name='api_job_detail'),
    path('categories/', views.CategoryListAPIView.as_view(), name='api_category_list'),
    path('applications/', views.MyApplicationsAPIView.as_view(), name='api_my_applications'),
]