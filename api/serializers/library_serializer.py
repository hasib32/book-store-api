from api.models import Library
from rest_framework import serializers


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = [
            'id',
            'created_by',
            'name',
            'address',
            'created_at',
            'updated_at']

        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'created_by': {'read_only': True},
        }
