from django.http import HttpResponse,HttpResponseRedirect
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render,get_object_or_404,render_to_response
from .models import Products,Category,Adl_Item,Adl_region,Adl_type,Adl_glossy
from django.views.generic import ListView,DetailView
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
now = datetime.datetime.now()
def homepage(request):
    content = {'所有类别': Adl_Item.objects.filter(due_time__gte = now),"now":datetime.datetime.now()}
    content['regions']=Adl_region.objects.all()
    content['types'] = Adl_type.objects.all()
    content['glossys']=Adl_glossy.objects.all()
    content['stocks'] = ['Yes']
    content['username'] = request.user.username

    # return  render(request,'home/index4.html',content)

    return  render(request, 'home/index.html', content)

@csrf_exempt
def adl_login(request):
    if request.method == 'POST':
        username =request.POST.get("username")
        password =request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                content = {'所有类别': Adl_Item.objects.filter(due_time__gte=now), "now": datetime.datetime.now()}
                content['regions'] = Adl_region.objects.all()
                content['types'] = Adl_type.objects.all()
                content['glossys'] = Adl_glossy.objects.all()
                content['stocks'] = ['Yes']
                content['username'] = request.user.username
                return render(request, 'home/index.html',content)

        content = {'reason':"用户名密码错误",'url':'/login','action':'重新登录'}
        return render(request, 'home/error.html', content)

    else:
        content = {}
        content['username'] = request.user.username
        print(content)

        return  render(request,'home/login.html')



@login_required(login_url='/login/')
def adl_logout(request):
    logout(request)
    content = {'reason': "注销成功", 'url': '/login', 'action': '重新登录'}
    return render(request, 'home/error.html', content)

#todo 修改密码界面的制作
# @login_required(login_url='/login/')
# def change_password(request):
#     if request.

@login_required(login_url='/login/')
def user_center(request):
    user = request.user
    print(user.has_perm('home.add_adl_item'))



@csrf_exempt
def search(request):
    if request.method == 'POST':
        print(request.POST)
    else:
        search_code = request.GET.get('search')
        content = {
            '所有类别': Adl_Item.objects.filter(due_time__gte=now).filter(name__icontains=search_code),
            "now": datetime.datetime.now()}
        content['regions'] = Adl_region.objects.all()
        content['types'] = Adl_type.objects.all()
        content['glossys'] = Adl_glossy.objects.all()
        content['username'] = request.user.username
        content['stocks'] = ['Yes']
        return render(request, 'home/index.html', content)


@csrf_exempt
def homepagefilter(request):
    if request.method == 'POST':
        print(request.POST)
        stock = request.POST.getlist("stock[]")
        region = request.POST.getlist("region[]")
        glossy = request.POST.getlist("glossy[]")
        type = request.POST.getlist("type[]")
        ret = {'code': '200'}
        ret['message'] = u'post成功'
        return HttpResponse(json.dumps(ret))

    else:
        region = request.GET.getlist('region')
        type = request.GET.getlist('type')
        glossy = request.GET.getlist('glossy')
        stock = request.GET.get('stock')
        # print(type(request.GET.get('stock')))
        print(stock)
        if stock ==None:
            content = {
                '所有类别': Adl_Item.objects.filter(due_time__gte=now).filter(adl_region__name__in=region).filter(
                    glossy_code__name__in=glossy).filter(adl_type__name__in=type).filter(stock__gt=1),
                "now": datetime.datetime.now()}
        else:
            content = {
                '所有类别': Adl_Item.objects.filter(due_time__gte=now).filter(adl_region__name__in=region).filter(
                    glossy_code__name__in=glossy).filter(adl_type__name__in=type).filter(stock__gte=0),
                "now": datetime.datetime.now()}


        content['regions'] = Adl_region.objects.all()
        content['types'] = Adl_type.objects.all()
        content['glossys'] = Adl_glossy.objects.all()
        content['username'] = request.user.username
        content['stocks'] = ['Yes']
        return render(request, 'home/index.html', content)
        # return HttpResponseRedirect('/')

    # content = {'所有类别': Adl_Item.objects.filter(due_time__gte = now).filter(stock__in=stock).filter(adl_region__in=region).filter(glossy_code__in=glossy).filter(adl_type__in=type),"now":datetime.datetime.now()}

    content = {'所有类别': Adl_Item.objects.filter(due_time__gte = now).filter(stock__gt=0),"now":datetime.datetime.now()}
    # return  render(request,'home/index4.html',content)


    return  render(request, 'home/index.html', content)




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

class Homelist(ListView):
    model = Category
    template_name = "home/index4.html"
    context_object_name = "Category"


class Homedetail(DetailView):
    model = Products
    template_name = "home/detail.html"
    context_object_name = "Product"



@csrf_exempt
def post_getdata(request):
    if request.method == 'POST':
        adl_id = request.POST['id']
        adl=Adl_Item.objects.get(pk=adl_id)
        ret={'code':'200'}
        ret['message']=u'post成功'
        ret['name'] = adl.name
        data=request.POST
        ret['result']=data

        return HttpResponse(json.dumps(ret))
    else:
        ret = {'code': '500'}
        ret['message'] = u'post失败!!!'
        return HttpResponse(json.dumps(ret))


@csrf_exempt
def post_getdata(request):
    if request.method == 'POST':
        adl_id = request.POST['id']
        adl=Adl_Item.objects.get(pk=adl_id)
        ret={'code':'200'}
        ret['message']=u'post成功'
        ret['name'] = adl.name
        ret['type'] = adl.adl_type.name
        ret['region'] = adl.adl_region.name
        ret['struct'] = adl.struct_code
        ret['glossy'] = adl.glossy_code.name
        ret['standard'] = adl.adl_standard
        ret['stock'] = adl.stock
        ret['create'] = adl.createtime.strftime("%Y-%m-%d")
        ret['due'] = adl.due_time.strftime("%Y-%m-%d")
        data=request.POST
        ret['result']=data

        return HttpResponse(json.dumps(ret))
    else:
        ret = {'code': '500'}
        ret['message'] = u'post失败!!!'
        return HttpResponse(json.dumps(ret))





def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return render_to_response(str(a+b))