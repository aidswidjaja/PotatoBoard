from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post, name='post'),
    path('logout/', views.logoutUser, name='logout'),
    path('all/', views.all, name='all'),
    path('manage/', views.manage, name='manage'),
    path('manage/push/', views.push, name='push'),
    path('manage/push/pipeline/', views.pipeline, name='pipeline'),
]