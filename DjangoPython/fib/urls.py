# pages/urls.py
from django.urls import path

from .views import homePageView, fib

urlpatterns = [
    path('', homePageView, name='home'),
    path('fib/<int:amt>', fib, name='home')

]