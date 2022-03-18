from api.models import Transaction
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=['rented', 'returned'], required=True)

    class Meta:
        model = Transaction
        fields = [
            'id',
            'user',
            'created_by',
            'status',
            'due_date',
            'book',
            'created_at',
            'updated_at']

        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'created_by': {'read_only': True},
        }
