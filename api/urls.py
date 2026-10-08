from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views

urlpatterns = [
    path('jobs/', views.JobListAPIView.as_view(), name='api_job_list'),
    path('jobs/<int:pk>/', views.JobDetailAPIView.as_view(), name='api_job_detail'),
    path('categories/', views.CategoryListAPIView.as_view(), name='api_category_list'),
    path('applications/', views.MyApplicationsAPIView.as_view(), name='api_my_applications'),

    path('auth/register/', views.RegisterAPIView.as_view(), name='api_register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('auth/refresh', TokenObtainPairView.as_view(), name='token_refresh'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]