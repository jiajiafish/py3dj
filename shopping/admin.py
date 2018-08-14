from .models import Products,Category
from django.contrib import admin
admin.site.site_header = "小米官方网站"

admin.site.site_title = "小米官方后台"



class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','picture','category','price','kucun','onshelf','Createtime','Modtime']
    list_editable = ['category','price','kucun']
    list_per_page = 10
    # save_as = True
    list_filter = ['category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','desc','picture']
    list_editable = ['desc']

# Register your models here.
admin.site.register(Products,ProductAdmin)
admin.site.register(Category)
