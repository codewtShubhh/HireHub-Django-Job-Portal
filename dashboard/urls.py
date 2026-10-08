from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('recruiter/', views.recruiter_dashboard_view, name='recruiter_dashboard'),
    path('seeker/', views.seeker_dashboard_view, name='seeker_dashboard'),
]