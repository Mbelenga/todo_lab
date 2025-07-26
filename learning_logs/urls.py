"""Defines URLs patterns for learning_logs."""

from Django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index')
]