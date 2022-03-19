from api.models import Transaction
from rest_framework import serializers
from .book_seralizer import BookSerializer


class TransactionBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = [
            'id',
            'due_date',
            'book',
            'created_at',
            'updated_at']
