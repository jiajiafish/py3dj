from django.conf.urls import re_path, url
from django.urls import re_path

from .views import MyView

urlpatterns = [re_path(r'^mine/$', MyView.as_view(), name='my-view')]


