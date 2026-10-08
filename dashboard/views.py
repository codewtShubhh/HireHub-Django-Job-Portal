from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jobs.models import Job
from applications.models import Application


@login_required
def dashboard_view(request):
    profile = getattr(request.user, 'profile', None)

    if profile is None:
        messages.error(request, 'Please complete your profile first.')
        return redirect('home')

    if profile.user_type == 'recruiter':
        return redirect('recruiter_dashboard')
    else:
        return redirect('seeker_dashboard')


@login_required
def recruiter_dashboard_view(request):
    company = getattr(request.user, 'Companies', None)

    if company is None:
        messages.info(request, 'Create your company profile to get started.')
        return redirect('company_create')

    jobs = Job.objects.filter(company=company).order_by('-created_at')
    total_applications = Application.objects.filter(job__company=company).count()

    context = {
        'company': company,
        'jobs': jobs,
        'total_applications': total_applications,
    }
    return render(request, 'dashboard/recruiter_dashboard.html', context)


@login_required
def seeker_dashboard_view(request):
    applications = Application.objects.filter(applicant=request.user).order_by('-applied_at')
    context = {
        'applications': applications,
    }
    return render(request, 'dashboard/seeker_dashboard.html', context)