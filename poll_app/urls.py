from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('make_poll', views.make_poll, name='make_poll'),
    path('vote/<int:poll_id>', views.vote, name='vote'),
    path('display_results/<int:poll_id>', views.display_results, name='display_results'),
    path('delete_poll/<int:poll_id>', views.delete_poll, name="delete_poll")
]
