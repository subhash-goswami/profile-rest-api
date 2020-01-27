from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('user/<str:aid>', views.display_name, name="display"),
    path('hello', views.hello, name="hello")


]
