from django.urls import path
from . import views

app_name = 'emojiTransApp'

urlpatterns = [
    path('', views.index, name='top'),
    path('form', views.form, name='form'),
    path('emoji', views.emoji),
    path('search', views.search),
    path('result', views.result)
]
