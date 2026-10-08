from django.urls import path
from . import views

urlpatterns = [
   path('create/', views.company_create_view, name='company_create'),
    path('', views.company_detail_view, name='company_detail'),
    path('edit/', views.company_edit_view, name='company_edit'),
]