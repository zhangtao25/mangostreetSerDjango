from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getnotebyid',views.get_note_by_id, name = 'get_note_by_id')
]