from django.urls import path
from . import views

app_name = 'crosslingual'

urlpatterns = [
    path('', views.index, name='top'),
    path('form', views.form, name='form'),
    path('result', views.result),
    path('visual', views.visual, name='visual')
]
