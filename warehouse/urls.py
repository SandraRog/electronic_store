"""
URL configuration for warehouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from store.views import PartListView, PartCreateView, PartUpdateView, PartDeleteView, CategoryListView, \
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView, CategoryDetailView, LocationCreateView, \
    LocationListView, LocationUpdateView, LocationDeleteView, LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    #parts
    path('parts/', PartListView.as_view(), name='part-list'),
    path('parts/create/', PartCreateView.as_view(), name='part-create'),
    path('parts/<int:pk>/update/', PartUpdateView.as_view(), name='part-update'),
    path('parts/<int:pk>/delete/', PartDeleteView.as_view(), name='part-delete'),
    #categories
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    #locations
    path('locations/', LocationListView.as_view(), name='locations-list'),
    path('locations/create/', LocationCreateView.as_view(), name='locations-create'),
    path('locations/<int:pk>/update/', LocationUpdateView.as_view(), name='locations-update'),
    path('locations/<int:pk>/delete/', LocationDeleteView.as_view(), name='locations-delete'),
    path('locations/<int:pk>/', CategoryDetailView.as_view(), name='locations-detail'),
]
