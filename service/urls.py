from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('contact/',views.contact,name='contact'),
    # path('send_contact',views.send_contact,name='send_contact')
    # path('', views.all_projects, name='all_projects'),
    # path('<int:project_id>', views.project_detail, name='project_detail'),
]
