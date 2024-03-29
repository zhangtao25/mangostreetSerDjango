from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notes import views

# 创建一个路由器并注册我们的视图集。
router = DefaultRouter()
router.register(r'notes', views.NoteViewSet, basename='notes')
router.register(r'likes', views.LikeViewSet, basename='likes')
router.register(r'collects', views.CollectViewSet)
router.register(r'images', views.ImageViewSet, basename='images')

# API url现在由路由器自动确定。
urlpatterns = [
    path('', include(router.urls)),
]
