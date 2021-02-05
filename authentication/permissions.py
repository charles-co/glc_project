from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return True
        
    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj.user == request.user
        return False