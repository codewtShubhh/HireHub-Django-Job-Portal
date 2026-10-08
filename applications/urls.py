from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_job_view, name='apply_job'),
    path('my-applications/', views.my_applications_view, name='my_applications'),
    path('job/<int:job_id>/applicants/', views.job_applicants_view, name='job_applicants'),
    path('status/<int:application_id>/update/', views.update_application_status_view, name='update_application_status'),
]