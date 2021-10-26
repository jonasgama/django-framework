from rest_framework import permissions


class SuperUserContacts(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'DELETE' is not request.user.is_superuser:
            return False
        return True
