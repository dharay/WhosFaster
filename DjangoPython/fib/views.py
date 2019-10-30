from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World!')

def fib(request,amt):
    return HttpResponse(calulateFib(amt))

def calulateFib(n):
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return calulateFib(n-1)+calulateFib(n-2) 
