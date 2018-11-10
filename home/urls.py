from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('1/', views.pg1, name="主页"),
    path('2/', views.pg2, name="主页"),
    path('3/', views.pg3, name="主页"),
    path('4/', views.pg4, name="主页"),
    path('5/', views.pg5, name="主页"),
    # path('add/', views.pg5, name="主页"),

    path('', views.homepage, name="主页"),
]
