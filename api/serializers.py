from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from django.utils import timezone
from users.models import Profile

from rest_framework import serializers
from jobs.models import Job, Category
from applications.models import Application
from companies.models import Companies


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    user_type = serializers.ChoiceField(choices=Profile.USER_TYPE, write_only=True)
    phone = serializers.CharField(max_length=15, required=False, allow_blank=True, default='', write_only=True)
    location = serializers.CharField(max_length=30, required=False, allow_blank=True, default='', write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'user_type', 'phone', 'location']

    @transaction.atomic
    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        phone = validated_data.pop('phone')
        location = validated_data.pop('location')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(
            user=user, user_type=user_type,
            phone=phone, location=location, skills=''
        )
        return user


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

    def validate_job(self, job):
        user = self.context['request'].user
        if not job.is_active:
            raise serializers.ValidationError('This job is no longer active.')
        if job.deadline and job.deadline < timezone.localdate():
            raise serializers.ValidationError('The deadline for this job has passed.')
        if Application.objects.filter(job=job, applicant=user).exists():
            raise serializers.ValidationError('You have already applied to this job.')
        return job