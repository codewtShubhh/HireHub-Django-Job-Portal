from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm
from companies.models import Companies


def _is_recruiter(user):
    profile = getattr(user, 'profile', None)
    return profile is not None and profile.user_type == 'recruiter'


def _get_company_or_redirect(request):
    """Returns (company, None) if found, or (None, redirect_response) if not."""
    try:
        company = Companies.objects.get(recruiter=request.user)
        return company, None
    except Companies.DoesNotExist:
        messages.info(request, 'Create your company profile to get started.')
        return None, redirect('company_create')


@login_required
def job_create_view(request):
    if not _is_recruiter(request.user):
        messages.error(request, 'Only recruiters can post jobs.')
        return redirect('home')

    company, redirect_response = _get_company_or_redirect(request)
    if redirect_response:
        return redirect_response

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company
            job.save()
            messages.success(request, 'Job posted successfully.')
            return redirect('company_jobs')
    else:
        form = JobForm()

    return render(request, 'jobs/job_form.html', {'form': form})


@login_required
def company_jobs_view(request):
    if not _is_recruiter(request.user):
        messages.error(request, 'Only recruiters can view this page.')
        return redirect('home')

    company, redirect_response = _get_company_or_redirect(request)
    if redirect_response:
        return redirect_response

    jobs = Job.objects.filter(company=company).order_by('-created_at')
    return render(request, 'jobs/company_jobs.html', {'jobs': jobs})


@login_required
def job_edit_view(request, job_id):
    if not _is_recruiter(request.user):
        messages.error(request, 'Only recruiters can edit jobs.')
        return redirect('home')

    company, redirect_response = _get_company_or_redirect(request)
    if redirect_response:
        return redirect_response

    job = get_object_or_404(Job, id=job_id, company=company)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully.')
            return redirect('company_jobs')
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/job_form.html', {'form': form})


@login_required
def job_delete_view(request, job_id):
    if not _is_recruiter(request.user):
        messages.error(request, 'Only recruiters can delete jobs.')
        return redirect('home')

    company, redirect_response = _get_company_or_redirect(request)
    if redirect_response:
        return redirect_response

    job = get_object_or_404(Job, id=job_id, company=company)

    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted.')
        return redirect('company_jobs')

    return render(request, 'jobs/job_confirm_delete.html', {'job': job})


def job_detail_view(request, job_id):
    job = get_object_or_404(Job, id=job_id, is_active=True)
    return render(request, 'jobs/job_detail.html', {'job': job})


def job_list_view(request):
    jobs = Job.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})