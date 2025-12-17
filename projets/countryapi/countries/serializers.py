# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 14:48:03 2025

@author: formation
"""

# countries/serializers.py
from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name", "capital", "area"]