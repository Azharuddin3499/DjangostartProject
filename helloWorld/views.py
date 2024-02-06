from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloworld(request):
    return HttpResponse('Hello World')


def hello(request):
    return render(request,'home.html',{'name':'Azhar'})