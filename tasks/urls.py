from django.urls import path
from . import views

urlpatterns = [
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('', views.index, name="list")
]
