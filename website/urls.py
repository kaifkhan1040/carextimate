from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('service',views.service,name='service'),
    path('about',views.about,name='aboutus'),
    path('tire',views.tire,name='tire'),
]