

# Register your models here.
from .models import Products,Category,Adl_Item,Adl_glossy,Adl_region,Adl_type
from django.contrib import admin
admin.site.site_header = "ADL平台"

admin.site.site_title = "ADL平台"



class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','eng_name','picture','category','Createtime','Modtime','site_url']
    list_editable = ['category','picture','site_url']
    list_per_page = 10
    # save_as = True
    list_filter = ['category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','picture','eng_name','site_url']
    list_editable = ['name','picture','site_url']


class Adl_itemAdmin(admin.ModelAdmin):
    list_display = ['id','name','adl_type','adl_region','struct_code','glossy_code','adl_standard','stock','createtime','picture','due_time']
    list_editable = ['adl_type']
    list_per_page = 10
    list_filter = ['adl_type']

class Adl_typeAdmin(admin.ModelAdmin):
    list_display = ['id','name','desc']
    list_per_page = 10

class Adl_glossyAdmin(admin.ModelAdmin):
    list_display = ['id','name','desc']
    list_per_page = 10


class Adl_regionAdmin(admin.ModelAdmin):
    list_display = ['id','name','desc']
    list_per_page = 10

# Register your models here.
# admin.site.register(Products,ProductAdmin)
# admin.site.register(Category,CategoryAdmin)
admin.site.register(Adl_Item,Adl_itemAdmin)
admin.site.register(Adl_type,Adl_typeAdmin)
admin.site.register(Adl_glossy,Adl_glossyAdmin)
admin.site.register(Adl_region,Adl_regionAdmin)