from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'phone', 'location', 'created_at')
    list_filter = ('user_type',)
    search_fields = ('user__username', 'phone', 'location')