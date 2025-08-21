from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    SAFE methods allowed for everyone.
    Write operations allowed only to the object's author.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj, 'author_id', None) == getattr(request.user, 'id', None)
