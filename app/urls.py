from django.urls import path
from app import views
urlpatterns=[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('calendar',views.calendar,name='calendar'),
]