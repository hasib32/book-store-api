from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class BaseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        auth_user = request.user
        model = self.get_object()
        model.delete(auth_user=auth_user)

        return Response(status=status.HTTP_204_NO_CONTENT)
