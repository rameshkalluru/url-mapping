from django.urls import path
from music import views

urlpatterns=[
    path('nag/',views.nag,name='nag'),
    path('nagu/',views.nagu,name='nagu'),
    path('nagaraju/',views.nagaraju,name='nagaraju'),
]