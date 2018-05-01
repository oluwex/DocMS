from rest_framework.permissions import BasePermission


class IsOwnProfileOrAdmin(BasePermission):

    message = "You can only view/update your profile."

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
        # print(request.user.)
        return obj == request.user or request.user.is_admin


class IsOwnProfile(BasePermission):

    message = "You can only view/update your profile."

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
        # print(request.user.)
        return obj == request.user

