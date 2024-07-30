from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):  # 전체 개체에 대한 권한
        if request.method == "GET":
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):  # 개별 개체에 대한 권한
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author
