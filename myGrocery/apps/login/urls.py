from django.urls import path
from apps.login import views

urlpatterns = [
    path('', views.loginuser, name='login'),
    path('user/', views.logoutuser, name='logout'),
    path('save', views.registration, name='registration'),

]
