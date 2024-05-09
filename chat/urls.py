from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('api/alarm/', views.alarm, name='alarm'),
    path('api/pos/', views.pos, name='pos'),
]
