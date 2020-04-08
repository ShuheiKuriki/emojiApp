from django.urls import path
from . import views

app_name = 'paper'

urlpatterns = [
    path('', views.index, name='index'),
    path('sort', views.sort, name='sort'),
    path('list/<str:sort>', views.PaperListView.as_view(), name='list'),
    path('create', views.PaperCreateView.as_view(), name='create'),
    path('<int:pk>/update', views.PaperUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/detail', views.PaperDetailView.as_view(), name='detail'),
]