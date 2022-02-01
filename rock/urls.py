from django.urls import path
from rock import views


urlpatterns=[
    path('lak/',views.lak,name='lak'),
    path('laks/',views.laks,name='laks'),
    path('laked/',views.laked,name='laked')
]