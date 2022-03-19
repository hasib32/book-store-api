from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

from api.models import User
from api.serializers import TransactionBookSerializer
from .view_helper import *


class UserBookList(APIView, LimitOffsetPagination):

    def get(self, request, *args, **kwargs):
        user_id = get_id_from_url_path(request.path)
        user = User.objects.filter(pk=user_id).first()
        if user is None:
            return Response(data={'details': 'requested user does not exists'}, status=404)

        if not request.user.is_admin and request.user.id != user.id:
            return Response(data={'detail': 'You do not have permission to perform this action'}, status=403)

        transaction_queryset = user.user_transactions.all()

        status = request.query_params.get('status')
        if status is not None:
            transaction_queryset = transaction_queryset.filter(status=status)

        due_date = request.query_params.get('due_date')
        if due_date is not None:
            transaction_queryset = transaction_queryset.filter(due_date__gte=due_date)

        ordering = request.query_params.get('ordering')
        if ordering:
            transaction_queryset = transaction_queryset.order_by(ordering)
        else:
            transaction_queryset = transaction_queryset.order_by('-due_date')

        results = self.paginate_queryset(transaction_queryset, request, view=self)
        serializer = TransactionBookSerializer(results, many=True)

        return self.get_paginated_response(serializer.data)
