from django.contrib import admin
from .models import Companies


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'recruiter', 'location', 'created_at')
    search_fields = ('company_name', 'recruiter__username')