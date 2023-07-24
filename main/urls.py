from django.urls import path
from main import views

urlpatterns = [
    path('', views.index),
    path('portfolio/', views.portfolio),
    path('languages/', views.languages),
    path('projects/', views.projects)
]