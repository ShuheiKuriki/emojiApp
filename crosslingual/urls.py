from django.urls import path
from . import views

app_name = 'crosslingual'

urlpatterns = [
    path('', views.index, name='top'),
    path('form', views.form, name='form'),
    path('result', views.result),
    path('translate_list', views.translate_list, name='list'),
    # path('make_table', views.make_table, name='make'),
    path('transition', views.transition, name='transition'),
    path('frequent_table/<str:src>/<str:tgt>', views.frequent_table, name='table')
]
