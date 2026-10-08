from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Companies
from .forms import CompanyForm


# Create your views here.

@login_required
def company_create_view(request):
    # prevent duplicate company profiles for the same recruiter
    if hasattr(request.user, 'Companies'):
        return redirect('company_detail')

    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.recruiter = request.user
            company.save()
            messages.success(request, 'Company profile created successfully.')
            return redirect('company_detail')
    else:
        form = CompanyForm()

    return render(request, 'companies/company_form.html', {'form': form})


@login_required
def company_detail_view(request):
    company = get_object_or_404(Companies, recruiter=request.user)
    return render(request, 'companies/company_detail.html', {'company': company})


@login_required
def company_edit_view(request):
    company = get_object_or_404(Companies, recruiter=request.user)

    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company profile updated.')
            return redirect('company_detail')
    else:
        form = CompanyForm(instance=company)

    return render(request, 'companies/company_form.html', {'form': form})
