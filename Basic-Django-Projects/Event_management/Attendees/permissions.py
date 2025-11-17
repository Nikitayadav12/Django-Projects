
from  rest_framework import  permissions


class IsAttendee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role=='attendees'
    #allow anyone to view (safe_method),restrict post to organizer

