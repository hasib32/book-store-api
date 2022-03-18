from rest_framework import generics, permissions

from api.models import Transaction
from api.serializers import TransactionSerializer


class TransactionList(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    ordering_fields = ['due_date']

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            queryset = Transaction.objects.all()
        else:
            # Non admin user can only see their transactions
            queryset = Transaction.objects.all().filter(pk=user.id)

        due_date = self.request.query_params.get('due_date')
        if due_date is not None:
            queryset = queryset.filter(due_date__gte=due_date)

        book_id = self.request.query_params.get('book_id')
        if book_id is not None:
            queryset = queryset.filter(book_id=book_id)

        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TransactionDetailPermission(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object or admin to edit/view it.
    """
    def has_object_permission(self, request, view, obj):
        # admin can access any object
        if request.user.is_admin:
            return True

        return obj.id == request.user.id


class TransactionDetail(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, TransactionDetailPermission]

