
from  rest_framework import  permissions


class IsOrganizerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role=='organizer'
    #allow anyone to view (safe_method),restrict post to organizer



    def has_object_permission(self, request, view,obj):
        #organizer can edit delete  only their own event
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.organizer==request.user