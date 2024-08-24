from django.urls import path
from . import views

urlpatterns = [
    path('create_trip/', views.create_trip, name='create_trip'),
    path('trip/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('', views.trip_list, name='trip_list'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.ustr_logout, name='logout'),
]
