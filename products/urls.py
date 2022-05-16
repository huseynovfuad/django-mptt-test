from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('catalog/list/', views.CatalogListView.as_view(), name='catalog-list'),
    path('category/list/<id>/', views.CategoryListView.as_view(), name='category-list'),
]