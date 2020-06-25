from django.urls import path
from . import views

"""
Url patterns that map/match app urls to views.
"""

urlpatterns = [
    path('', views.post_list, name='post_list'),
]