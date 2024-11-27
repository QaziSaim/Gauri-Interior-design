from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('',views.contact,name='contact'),
    path('about_home',views.about_home,name="about_home"),
    path('service_home',views.service_home,name='service_home')
]
