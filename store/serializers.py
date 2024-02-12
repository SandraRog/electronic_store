from rest_framework import serializers
from .models import Category, Location, Part


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent_category']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'room', 'bookcase', 'shelf', 'cupboard', 'column', 'row']


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ['id', 'serial_number', 'name', 'description', 'category', 'quantity', 'price', 'location']


