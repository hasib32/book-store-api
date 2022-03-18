from rest_framework import generics, filters

from api.models import Library
from api.serializers import BookSerializer
from django.http import Http404


def get_id_from_url_path(path):
    url_as_array = path.split("/")
    user_id = [int(item) for item in url_as_array if item.isdigit()]
    return user_id[0]


class LibraryBookList(generics.ListAPIView):
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'author']

    def get_queryset(self):
        library_id = get_id_from_url_path(self.request.path)
        library = Library.objects.filter(pk=library_id).first()
        if library is None:
            raise Http404('Library does not exist')

        author = self.request.query_params.get('author')
        queryset = library.books.all()

        if author is not None:
            queryset = queryset.filter(author=author)

        return queryset





