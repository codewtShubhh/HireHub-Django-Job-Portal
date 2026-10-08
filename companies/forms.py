from django import forms
from .models import Companies

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = [
            'company_name',
            'description',
            'website',
            'location',
            'logo',
        ]