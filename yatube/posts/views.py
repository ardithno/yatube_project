from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Это индекс')

def group_posts(request, slug):
    return HttpResponse('Это группы')
