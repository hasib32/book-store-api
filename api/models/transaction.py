from django.conf import settings
from django.db import models

from .book import Book


class TransactionManager(models.Manager):
    def create_transaction(self, book, **extra_fields):
        """

        :param book:
        :param extra_fields:
        :return: Transaction
        """
        book.status = Book.STATUS_RENTED
        book.save()

        return self.create(book=book, **extra_fields)


class Transaction(models.Model):
    status = models.CharField(max_length=255)
    book = models.ForeignKey('api.Book', on_delete=models.CASCADE, related_name='book_transactions')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_transactions'
    )
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transaction_created_by',
        blank=True
    )

    objects = TransactionManager()

    def __str__(self):
        return self.status
