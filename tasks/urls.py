from django.urls import path
from . import views

urlpatterns = [
    path('update/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete_task"),
    path('', views.index, name="list")
]
