from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World! from Django!')

def fib(request,amt):
    return HttpResponse(calulateFib(amt))

def calulateFib(n):
    if n==0 or n == 1: 
        return n
    else: 
        return calulateFib(n-1)+calulateFib(n-2) 
