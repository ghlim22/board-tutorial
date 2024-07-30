import rest_framework.request
from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
    """
    GET: everyone
    PUT/PATCH: owner
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
