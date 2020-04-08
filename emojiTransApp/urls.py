from django.urls import path
from . import views

app_name = 'emojiTransApp'

urlpatterns = [
    path('', views.index, name='top'),
    path('form', views.form, name='form'),
    path('result', views.result),
    path('visual/', views.visualize, name="visual"),
]