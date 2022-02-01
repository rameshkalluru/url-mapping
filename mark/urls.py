from django.urls import path
from mark import views

urlpatterns=[
    path('hello/',views.hello,name='hello'),
    path('images/',views.images,name='images'),
    path('REELS/',views.REELS,name='REELS')
]