"""emojiApp URL Configuration

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
from django.urls import path, include
from . import views

app_name = 'cross-lingual'

urlpatterns = [
    path('', views.index, name="top"),
    path('admin/', admin.site.urls),
    path('emojiTransApp/', include('emojiTransApp.urls')),
    path('crosslingual/', include('crosslingual.urls')),
    path('visual/', views.visualize, name="visual"),
    path('emoji/<foo>', views.emoji),
    path('form', views.render_form),
    path('login', views.login)
]
