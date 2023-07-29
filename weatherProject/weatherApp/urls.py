from django.contrib import admin
from django.urls import path
from weatherApp import views # from . import views

urlpatterns =[
    path('',views.search, name='search')
]