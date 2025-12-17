# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 14:52:12 2025

@author: formation
"""

# countries/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet

router = DefaultRouter()
router.register(r"countries", CountryViewSet)
urlpatterns = [
    path("", include(router.urls))
]
#router = DefaultRouter(trailing_slash=False)