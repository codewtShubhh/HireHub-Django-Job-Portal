from rest_framework.permissions import BasePermission

def get_user_type(user):
    profile = getattr(user, 'profile', None)
    return profile.user_type if profile else None

class IsJobSeeker(BasePermission):
    message = 'Only job seeker can do this.'

    def has_permission(self, request, view):
        return request.user.is_authenticated and get_user_type(request.user) == 'job_seeker'

class IsRecruiter(BasePermission):
    message = 'Only recruiters can do this.'

    def has_permission(self, request, view):
        return request.user.is_authenticated and get_user_type(request.user) == 'recruiter'