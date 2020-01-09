from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('emoji', views.emoji),
    path('search', views.search),
    path('result', views.result)
]
