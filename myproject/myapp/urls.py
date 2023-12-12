# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp.views import my_view  # Import your view
from myapp.views import success_view
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', my_view, name='home'),  # Add this line for the root path
    path('my_view/', my_view, name='my_view'),
    path('success/', success_view, name='success')

]
