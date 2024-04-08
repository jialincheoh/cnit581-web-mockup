from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name = 'task-home'),
    path('dashboard/', views.dashboard, name = 'task-dashboard'),
]