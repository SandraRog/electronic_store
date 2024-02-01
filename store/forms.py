from django import forms
from store.models import Category, Part, Location


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = '__all__'


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
