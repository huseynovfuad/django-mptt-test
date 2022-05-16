from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']



    def get_subcategories(self, obj):
        cat_list = []
        queryset = Category.objects.filter(parent=obj).order_by('name')
        cat_list = [{'id': qs.id, 'name': qs.name} for qs in queryset]
        return cat_list