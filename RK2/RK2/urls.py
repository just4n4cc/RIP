"""RK2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('book/', views.book_list),
    path('book/create', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete', views.BookDelete.as_view(), name='book_delete'),
    path('library/', views.lib_list),
    path('library/create', views.LibCreate.as_view(), name='lib_create'),
    path('library/<int:pk>/update', views.LibUpdate.as_view(), name='lib_update'),
    path('library/<int:pk>/delete', views.LibDelete.as_view(), name='lib_delete'),
    path('report/', views.report),
]
