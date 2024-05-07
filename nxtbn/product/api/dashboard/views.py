from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions  import AllowAny
from rest_framework.exceptions import APIException

from nxtbn.core.paginator import NxtbnPagination
from nxtbn.product.models import Product, Category, Collection
from nxtbn.product.api.dashboard.serializers import ProductSerializer, CategorySerializer, CollectionSerializer, RecursiveCategorySerializer
from nxtbn.core.admin_permissions import NxtbnAdminPermission



class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = NxtbnPagination


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (NxtbnAdminPermission,)
    lookup_field = 'id'


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(parent=None) # Get only top-level categories
    serializer_class = RecursiveCategorySerializer
    pagination_class = None


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (NxtbnAdminPermission,)
    lookup_field = 'id'


class CollectionListView(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (NxtbnAdminPermission,)
    pagination_class = None


class CollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (NxtbnAdminPermission,)
    lookup_field = 'id'
