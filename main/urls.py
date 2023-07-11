from django.urls import path
from main import views

urlpatterns = [
    path('', views.index),
    path('portfolio/', views.portfolio),
    path('lang/', views.lang),
    path('projects/', views.projects)
]