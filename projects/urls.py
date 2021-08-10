__author__ = 'Robert W. Curtiss'

"""
====================================================
Author: Robert W. Curtiss
    Project: 
    File: urls
    Created: Aug, 08, 2021
    
    Description:
    
===================================================
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>", views.project_detail, name="project_detail"),
]
