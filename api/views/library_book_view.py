from rest_framework import generics

from api.models import Library
from api.serializers import BookSerializer
from django.http import Http404


def get_id_from_url_path(path):
    url_as_array = path.split("/")
    user_id = [int(item) for item in url_as_array if item.isdigit()]
    return user_id[0]


class LibraryBookList(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        library_id = get_id_from_url_path(self.request.path)
        library = Library.objects.filter(pk=library_id).first()
        if library is None:
            raise Http404('Library does not exist')

        return library.books.all()



