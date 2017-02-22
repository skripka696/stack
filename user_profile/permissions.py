from rest_framework.permissions import BasePermission


class IsHaveAccess(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_superuser:
            return True
        elif hasattr(request.user, 'groups'):
            if request.user \
                   and 'moderators' in request.user.groups.all().values_list('name', flat=True) \
                   and request.user.is_staff:
                return True
        if not request.user.is_anonymous():
            if request.user and \
                   request.user == obj.user:
                return True
        else:
            return False