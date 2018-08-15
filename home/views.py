from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,get_object_or_404,render_to_response
from .models import Products,Category
# Create your views here.
def homepage(request):
    content = {'所有类别': Category.objects.all()}
    return  render(request,'home/index4.html',content)


def pg1(request):
    content = {'所有类别': Products.objects.filter(category = Category.objects.get(pk=1)),"name":Category.objects.get(pk=1).name,"eng_name":Category.objects.get(pk=1).eng_name,}
    return  render(request,'home/detail.html',content)

def pg2(request):
    content = {'所有类别': Products.objects.filter(category = Category.objects.get(pk=2)),"name":Category.objects.get(pk=2).name,"eng_name":Category.objects.get(pk=2).eng_name,}
    return  render(request,'home/detail.html',content)

def pg3(request):
    content = {'所有类别': Products.objects.filter(category = Category.objects.get(pk=3)),"name":Category.objects.get(pk=3).name,"eng_name":Category.objects.get(pk=3).eng_name,}
    return  render(request,'home/detail.html',content)

def pg4(request):
    content = {'所有类别': Products.objects.filter(category = Category.objects.get(pk=4)),"name":Category.objects.get(pk=4).name,"eng_name":Category.objects.get(pk=4).eng_name,}
    return  render(request,'home/detail.html',content)

def pg5(request):
    content = {'所有类别': Products.objects.filter(category = Category.objects.get(pk=5)),"name":Category.objects.get(pk=5).name,"eng_name":Category.objects.get(pk=5).eng_name,}
    return  render(request,'home/detail.html',content)


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return render_to_response(str(a+b))