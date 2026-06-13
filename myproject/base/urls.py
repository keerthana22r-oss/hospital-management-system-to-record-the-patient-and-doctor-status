from django.urls import path 
from . import views 
urlpatterns=[ 
path('home/',views.home, name='home'), 
path('',views.read_hospital,name='read_hospital'),
path('update_hospital/<int:pk>/',views.update_hospital,name='update_hospital'),
path('delete_hospital/<int:pk>/',views.delete_hospital,name='delete_hospital'),
]