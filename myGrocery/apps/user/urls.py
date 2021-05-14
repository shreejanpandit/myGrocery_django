from django.contrib import admin
from django.urls import path
from apps.user import views

urlpatterns = [
    path('', views.index, name='user'),
    path("update/", views.update, name="update"),
]
