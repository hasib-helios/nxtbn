from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions  import AllowAny
from rest_framework.exceptions import APIException


from nxtbn.core.admin_permissions import NxtbnAdminPermission
from nxtbn.order.models import Order
from .serializers import OrderSerializer
from nxtbn.core.paginator import NxtbnPagination

class OrderListView(generics.ListAPIView):
    permission_classes = (NxtbnAdminPermission,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = NxtbnPagination


class OrderDetailView(generics.RetrieveAPIView):
    permission_classes = (NxtbnAdminPermission,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
