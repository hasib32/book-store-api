from rest_framework import generics, filters
from django.http import Http404

from api.models import Library
from api.serializers import BookSerializer
from .view_helper import *


class LibraryBookList(generics.ListAPIView):
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'author']

    def get_queryset(self):
        library_id = get_id_from_url_path(self.request.path)
        library = Library.objects.filter(pk=library_id).first()
        if library is None:
            raise Http404('Library does not exist')

        queryset = library.books.all()

        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author=author)

        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)

        return queryset
