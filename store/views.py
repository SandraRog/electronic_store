from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework.generics import RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from store.forms import CategoryForm, PartForm, LocationForm
from store.models import Part, Category, Location
from django.contrib import messages
from rest_framework import generics, status
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

class PartDetailView(View):
    def get(self, request, pk):
        part_detail = Part.objects.filter(pk=pk)
        return render(request, 'part_detail.html', {'parts': part_detail})


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
        category_detail = Category.objects.filter(pk=pk)
        return render(request, 'category_detail.html', {'categories': category_detail})



# CRUD location
class LocationListView(View):
    def get(self, request):
        locations = Location.objects.all()
        return render(request, 'location_list.html', {'locations': locations})

class LocationDetailView(View):
    def get(self, request, pk):
        location_detail = Location.objects.filter(pk=pk)
        return render(request, 'location_detail.html', {'locations': location_detail})

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

#API GET list

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class PartList(generics.ListAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

#API GET details
class PartDetail(RetrieveAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    lookup_field = 'pk'

class CategoryDetail(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

class LocationDetail(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'pk'

#API delete
class PartDelete(APIView):
    def delete(self, request, pk):
        try:
            part = Part.objects.get(pk=pk)
        except Part.DoesNotExist:
            return Response({"error": "Part not found"}, status=status.HTTP_404_NOT_FOUND)

        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryDelete(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_destroy(self, instance):
        self.check_category_constraints(instance)
        instance.delete()

    def check_category_constraints(self, category):
        if category.part_set.exists():
            raise ValidationError("Nie można usunąć kategorii z przypisanymi częściami.")

        if category.parent_category and Category.objects.filter(parent_category=category.parent_category).exclude(pk=category.pk).exists():
            raise ValidationError("Nie można usunąć kategorii rodzica, która ma inne podkategorie.")

class LocationyDelete(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def perform_destroy(self, instance):
        self.check_category_constraints(instance)
        instance.delete()

    def check_category_constraints(self, location):
        if location.part_set.exists():
            raise ValidationError("Nie można usunąć lokalizacji z przypisanymi częściami.")

        # if location.parent_category and Location.objects.filter(parent_category=location.parent_category).exclude(
        #         pk=location.pk).exists():
        #     raise ValidationError("Nie można usunąć kategorii rodzica, która ma inne podkategorie.")