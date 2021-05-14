from django.urls import path
from apps.product import views

urlpatterns = [
    path('add/', views.add, name='add_product'),
    path('show/', views.see_category, name='see_category'),
    path('show_manage/', views.see_product, name='see_product'),
    path('', views.manage, name='manage_product'),
    path('delete/<int:pk>', views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),

]
