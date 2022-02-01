from django.urls import path
from mass import views

urlpatterns=[
    path('charan/',views.charan,name='charan'),
    path('kittu/',views.kittu,name='kittu'),
    path('ramesh/',views.ramesh,name='ramesh'),
]