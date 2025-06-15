from django.urls import path
from . import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('',views.service,name='service'), 
    path('dropdown',views.dropdown,name='dropdown'),
    path('about',views.about,name='aboutus'),
    path('tire',views.tire,name='tire'),
]