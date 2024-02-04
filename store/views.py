from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from store.forms import CategoryForm, PartForm, LocationForm
from store.models import Part, Category, Location
from django.contrib import messages
from rest_framework import generics
from .serializers import CategorySerializer, LocationSerializer, PartSerializer


class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html')


# CRUD part
class PartListView(View):
    def get(self, request):
        parts = Part.objects.all()
        locations = Location.objects.all()
        return render(request, 'part_list.html', {'parts': parts, 'locations': locations})


class PartCreateView(View):
    def get(self, request):
        form = PartForm()
        locations = Location.objects.all()
        return render(request, 'part_form.html', {'form': form, 'locations': locations})

    def post(self, request):
        form = PartForm(request.POST)
        locations = Location.objects.all()
        if form.is_valid():
            form.save()
            return redirect('part-list')
        return render(request, 'part_form.html', {'form': form, 'locations': locations})


class PartUpdateView(View):
    def get(self, request, pk):
        part = get_object_or_404(Part, pk=pk)
        form = PartForm(instance=part)
        locations = Location.objects.all()
        return render(request, 'part_update.html', {'form': form, 'locations': locations})

    def post(self, request, pk):
        part = get_object_or_404(Part, pk=pk)
        form = PartForm(request.POST, instance=part)
        locations = Location.objects.all()
        if form.is_valid():
            form.save()
            return redirect('part-list')
        return render(request, 'part_update.html', {'form': form, 'locations': locations})


class PartDeleteView(View):
    def get(self, request, pk):
        part = get_object_or_404(Part, pk=pk)
        locations = Location.objects.all()
        return render(request, 'part_confirm_delete.html', {'part': part, 'locations': locations})

    def post(self, request, pk):
        part = get_object_or_404(Part, pk=pk)
        answer = request.POST.get('answer')
        if answer == 'Yes':
            part.delete()
            return redirect('part-list')
        else:
            return redirect('part-list')


# CRUD category
class CategoryCreateView(View):
    def get(self, request):
        form = CategoryForm()
        categories = Category.objects.all()
        return render(request, 'category_form.html', {'form': form, 'categories': categories})

    def post(self, request):
        form = CategoryForm(request.POST)
        categories = Category.objects.all()
        if form.is_valid():
            form.save()
            return redirect('category-list')
        return render(request, 'category_form.html', {'form': form, 'category': categories})


class CategoryUpdateView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(instance=category)
        return render(request, 'category_update.html', {'form': form})

    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category-list')
        return render(request, 'category_update.html', {'form': form})


class CategoryDeleteView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        return render(request, 'category_confirm_delete.html', {'category': category})

    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        answer = request.POST.get('answer')
        if answer == 'Yes':
            try:
                category.delete()
                messages.success(request, 'Kategoria została pomyślnie usunięta.')
                return redirect('category-list')
            except ProtectedError:
                messages.error(request, 'Nie można usunąć kategorii z przypisanymi częściami lub podkategoriami.')
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, 'Operacja usuwania została anulowana.')
        return render(request, 'category_confirm_delete.html', {'category': category})


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'category_list.html', {'categories': categories})


class CategoryDetailView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        return render(request, 'category_detail.html', {'category': category})


# CRUD location
class LocationListView(View):
    def get(self, request):
        locations = Location.objects.all()
        return render(request, 'location_list.html', {'locations': locations})


class LocationCreateView(View):
    def get(self, request):
        form = LocationForm()
        locations = Location.objects.all()
        return render(request, 'location_form.html', {'form': form, 'locations': locations})

    def post(self, request):
        form = LocationForm(request.POST)
        locations = Location.objects.all()
        if form.is_valid():
            form.save()
            return redirect('locations-list')
        return render(request, 'location_form.html', {'form': form, 'locations': locations})


class LocationUpdateView(View):
    def get(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        form = LocationForm(instance=location)
        return render(request, 'location_update.html', {'form': form})

    def post(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('locations-list')
        return render(request, 'location_update.html', {'form': form})


class LocationDeleteView(View):
    def get(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        return render(request, 'location_confirm_delete.html', {'location': location})

    def post(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        answer = request.POST.get('answer')
        if answer == 'Yes':
            try:
                location.delete()
                return redirect('locations-list')
            except ProtectedError:
                messages.error(request, 'Nie można usunąć lokalizacji z przypisanymi częściami.')
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, 'Operacja usuwania została anulowana.')
        return render(request, 'location_confirm_delete.html', {'location': location})

#API

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class PartList(generics.ListAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer