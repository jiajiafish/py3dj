from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context