from django.contrib import admin
from .models import Category
from mptt.admin import MPTTModelAdmin
# Register your models here.


admin.site.register(Category, MPTTModelAdmin)
