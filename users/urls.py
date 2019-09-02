from django.urls import path

from . import views

urlpatterns = [
    path('reg/', views.reg, name='reg'),
    path('vcode/', views.vcode, name='vcode')
]