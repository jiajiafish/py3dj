
# Create your views here.
from django.shortcuts import render,get_object_or_404
from .models import Products,Category
# Create your views here.
def homepage(request):
    content = {'所有类别': Category.objects.all()}
    return  render(request,'home/index4.html',content)


def pg1(request):
    content = {'所有类别': Products.objects.filter(category = Category.objects.get(pk=1))}
    return  render(request,'home/detail.html',content)

def pg2(request):
    content = {'所有类别': Products.objects.filter(category = Category.objects.get(pk=2))}
    return  render(request,'home/detail.html',content)

def pg3(request):
    content = {'所有类别': Products.objects.filter(category = Category.objects.get(pk=3))}
    return  render(request,'home/detail.html',content)

def pg4(request):
    content = {'所有类别': Products.objects.filter(category = Category.objects.get(pk=4))}
    return  render(request,'home/detail.html',content)

def pg5(request):
    content = {'所有类别': Products.objects.filter(category = Category.objects.get(pk=5))}
    return  render(request,'home/detail.html',content)