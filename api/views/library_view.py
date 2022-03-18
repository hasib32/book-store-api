from rest_framework import generics

from api.models import Library
from api.serializers import LibrarySerializer


class LibraryList(generics.ListCreateAPIView):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class LibraryDetail(generics.RetrieveAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
