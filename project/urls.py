from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('<int:project_id>', views.project_detail, name='project_detail'),
]
