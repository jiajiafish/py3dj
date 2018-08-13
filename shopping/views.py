from django.shortcuts import render,get_object_or_404
from .models import Products,Category
# Create your views here.
def homepage(request):
    content = {'所有商品': Products.objects.all()}
    return  render(request,'shopping/home.html',content)