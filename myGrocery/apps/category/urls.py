from django.urls import path
from apps.category import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cat/', views.see_category, name='see_category'),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),
]
