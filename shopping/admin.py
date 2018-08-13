from .models import Products,Category
from django.contrib import admin



class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','picture','category','price','kucun','onshelf','Createtime','Modtime']
    list_editable = ['category','price','kucun']
    list_per_page = 10


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','desc','picture']
# Register your models here.
admin.site.register(Products,ProductAdmin)
admin.site.register(Category)
