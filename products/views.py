from rest_framework import generics
from .serializers import Category, CategorySerializer
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

########################################################
###  1. Catalog                                      ###
###       1.1. Category                              ###
###            1.1.2 SubCategory                     ###
########################################################


class CatalogListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.filter(parent=None).order_by('name')
        return queryset




class CategoryListView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        queryset = Category.objects.filter(parent=obj).order_by('name')
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=200)