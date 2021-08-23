from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results', views.results, name='results'),
    path('add_operation', views.add_operation, name='add_operation'),
    path('calculate', views.calculate, name = 'calculate'),
]