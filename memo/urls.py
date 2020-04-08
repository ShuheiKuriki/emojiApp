from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
    path('', views.MemoListView.as_view(), name='index'),
    path('create', views.MemoCreateView.as_view(), name='create'),
    path('<int:pk>/update', views.MemoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/detail', views.MemoDetailView.as_view(), name='detail'),
]