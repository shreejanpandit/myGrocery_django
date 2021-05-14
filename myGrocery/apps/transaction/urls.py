from django.urls import path
from apps.transaction import views

urlpatterns = [
    path('create', views.create, name='add_product'),
    path('', views.manage, name='manage_product'),
    path("delete/<int:pk>", views.delete, name="delete"),
    path('show_prod_cat/', views.see_product_category, name='see_product_category'),
    # path('show_cat/', views.see_category, name='see_category'),
]
