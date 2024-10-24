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
from django.conf import settings
from django.conf.urls.static import static

from Backend.views import CategoryView, ContactView, LoginView, RegisterView, SubtasksView, TaskView

urlpatterns = [
    path('', ContactView.as_view()),
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view()),
    path('task/', TaskView.as_view()),
    path('task/<int:pk>/', TaskView.as_view(), name='task-detail'),
    path('login/', LoginView.as_view()),
    path('contact/', ContactView.as_view()),
    path('contact/<int:pk>/', ContactView.as_view(), name='contact-detail'),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryView.as_view(), name='category-detail'),
    path('subtask/', SubtasksView.as_view(), name='category-detail'),
    path('subtask/<int:pk>/', SubtasksView.as_view(), name='subtask-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
