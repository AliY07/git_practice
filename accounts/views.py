from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.template import loader
from django.shortcuts import render

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def first_page(request):
    template = loader.get_template('shop/first_page.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)

def products(request):
    template = loader.get_template('shop/products.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)

def deals(request):
    template = loader.get_template('shop/deals.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)

def stores(request):
    template = loader.get_template('shop/stores.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)

def contact(request):
    template = loader.get_template('shop/contact.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)