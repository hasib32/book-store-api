from rest_framework import generics, permissions

from api.models import User
from api.serializers import UserSerializer
from rest_framework.response import Response


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            # admin user can access all the records
            return User.objects.all()
        else:
            return User.objects.all().filter(pk=user.id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class UserDetailPermission(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object or admin to edit/view it.
    """
    def has_object_permission(self, request, view, obj):
        # admin can access any object
        if request.user.is_admin:
            return True

        return obj.id == request.user.id


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, UserDetailPermission]


class AuthUserDetail(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
