from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('skills/', views.skills, name= 'skills'),
    path('projects/', views.projects, name = 'projects'),
]


