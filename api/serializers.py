from rest_framework import serializers
from jobs.models import Job, Category
from applications.models import Application
from companies.models import Companies


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ['id', 'company_name', 'description', 'website', 'location', 'logo']


class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Job
        fields = [
            'id', 'company', 'category', 'title', 'description', 'location',
            'salary_min', 'salary_max', 'experience', 'job_type', 'skills',
            'deadline', 'is_active', 'created_at', 'updated_at'
        ]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'id', 'job', 'applicant', 'resume', 'cover_letter',
            'status', 'applied_at', 'updated_at'
        ]
        read_only_fields = ['applicant', 'status', 'applied_at', 'updated_at']