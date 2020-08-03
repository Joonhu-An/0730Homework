"""Blogproject0730 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import post.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", post.views.main, name="main"),
    path("new/", post.views.new, name="new"),
    path("create/", post.views.create, name="create"),
    path("detail/<int:blog_id>", post.views.detail, name="detail"),
    path("delete/<int:blog_id>", post.views.delete, name="delete"),
    path("update/<int:blog_id>", post.views.update, name="update"),
    path("renew/<int:blog_id>", post.views.renew, name="renew"),
]
