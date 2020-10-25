from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('population-chart/', views.population_chart, name='population-chart'),
]