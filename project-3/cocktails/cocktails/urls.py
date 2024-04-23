"""
URL configuration for cocktails project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('experiment/', include('experiment.urls')),
    path('register/', user_views.signup, name='register'),
    path('login/', user_views.signin, name='signin'),
    path('', user_views.signin, name='signin'),
    path('task1/', user_views.task1, name='task1'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('save-user-input/', user_views.save_user_input, name='save_user_input'),
    path('task2/', user_views.task2, name='task2'),
    path('task3/', user_views.task3, name='task3'),
    path('task4/', user_views.task4, name='task4'),
    path('task5/', user_views.task5, name='task5'),
    path('task6/', user_views.task6, name='task6'),
    path('final/', user_views.final, name='final'),
]