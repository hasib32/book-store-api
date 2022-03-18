from django.conf import settings
from django.db import models


class Book(models.Model):
    library = models.ForeignKey('api.Library', on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='book_created_by',
        blank=True
    )

    def __str__(self):
        return self.title
