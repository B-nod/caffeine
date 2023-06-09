from dataclasses import fields
import django_filters
from products.models import *
from django_filters import CharFilter

class ProductFilter(django_filters.FilterSet):
    product_name_contains= CharFilter(field_name='product_name', lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ''
        exclude = ['product_price','stock','image','description','created_at','category']

class CategoryFilter(django_filters.FilterSet):
    category_name_contains= CharFilter(field_name='category_name', lookup_expr='icontains')
    class Meta:
        model = Category
        fields = ''
       