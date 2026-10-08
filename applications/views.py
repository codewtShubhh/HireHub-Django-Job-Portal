from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Application
from .forms import ApplicationForm
from jobs.models import Job


@login_required
def apply_job_view(request, job_id):
    job = get_object_or_404(Job, id=job_id, is_active=True)

    # prevent duplicate applications
    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.info(request, 'You already applied to this job.')
        return redirect('job_detail', job_id=job.id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, 'Application submitted successfully.')
            return redirect('my_applications')
    else:
        form = ApplicationForm()

    return render(request, 'applications/apply_form.html', {'form': form, 'job': job})


@login_required
def my_applications_view(request):
    applications = Application.objects.filter(applicant=request.user).order_by('-applied_at')
    return render(request, 'applications/my_applications.html', {'applications': applications})


@login_required
def job_applicants_view(request, job_id):
    job = get_object_or_404(Job, id=job_id, company__recruiter=request.user)
    applications = Application.objects.filter(job=job).order_by('-applied_at')
    return render(request, 'applications/job_applicants.html', {'job': job, 'applications': applications})


@login_required
def update_application_status_view(request, application_id):
    application = get_object_or_404(
        Application,
        id=application_id,
        job__company__recruiter=request.user
    )

    if request.method == 'POST':
        status = request.POST.get('status')
        if status in dict(Application.STATUS_CHOICES):
            application.status = status
            application.save()
            messages.success(request, 'Application status updated.')

    return redirect('job_applicants', job_id=application.job.id)