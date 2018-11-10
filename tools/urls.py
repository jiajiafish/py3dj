from django.urls import path,re_path
# from . import views
from tools import views

app_name = "tools"

urlpatterns = [
    path('',views.index,name = 'tools')
]