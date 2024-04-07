"""
URL configuration for Join_Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from Backend.views import CategoryView, ContactView, LoginView, RegisterView, TaskView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view()),
    path('tasks/', TaskView.as_view()),
    path('login/', LoginView.as_view()),
    path('contact/', ContactView.as_view()),
    path('contact/<int:pk>/', ContactView.as_view(), name='contact-detail'),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryView.as_view(), name='category-detail'),
]
