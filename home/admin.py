

# Register your models here.
from .models import Products,Category
from django.contrib import admin
admin.site.site_header = "数字化平台后台"

admin.site.site_title = "数字化平台后台"



class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','eng_name','picture','category','Createtime','Modtime','site_url']
    list_editable = ['category','picture','site_url']
    list_per_page = 10
    # save_as = True
    list_filter = ['category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','picture','eng_name','site_url']
    list_editable = ['name','picture','site_url']

# Register your models here.
admin.site.register(Products,ProductAdmin)
admin.site.register(Category,CategoryAdmin)