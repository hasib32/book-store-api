from api.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=['available', 'rented'], required=False)

    class Meta:
        model = Book

        fields = [
            'id',
            'created_by',
            'library',
            'title',
            'author',
            'isbn',
            'status',
            'created_at',
            'updated_at']

        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'created_by': {'read_only': True},
            'status': {'choices'}
        }
