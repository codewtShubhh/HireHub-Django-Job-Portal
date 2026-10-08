from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list_view, name='job_list'),
    path('create/', views.job_create_view, name='job_create'),
    path('my-jobs/', views.company_jobs_view, name='company_jobs'),
    path('<int:job_id>/', views.job_detail_view, name='job_detail'),
    path('<int:job_id>/edit/', views.job_edit_view, name='job_edit'),
    path('<int:job_id>/delete/', views.job_delete_view, name='job_delete'),
]