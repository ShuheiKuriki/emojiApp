from django.urls import path
from . import views

app_name = 'crosslingual'

urlpatterns = [
    path('', views.index, name='top'),
    path('form', views.form, name='form'),
    path('result', views.result),
    path('translate_list', views.translate_list, name='list')
]
