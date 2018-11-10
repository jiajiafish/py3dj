from django.conf.urls import url
from snippets import views
from django.urls import path, include,re_path

urlpatterns = [
    re_path(r'snippets/$', views.snippet_list),
    re_path(r'snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]