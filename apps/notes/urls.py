from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.get_all, name ='get_all'),
    path('<str:id>/', views.get_by_id, name ='get_by_id')
]