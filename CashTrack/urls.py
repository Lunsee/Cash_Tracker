"""
URL configuration for CashTrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from cash_tracker import views


urlpatterns = [
    path('admin/', admin.site.urls),

    #Запрос для формирования списка подкатегорий для "Категории"
    path('subcategory-autocomplete/', views.SubcategoryAutocomplete.as_view(), name='subcategory-autocomplete'),

    #Запрос для формирования списка категории для списка "Тип"
    path('category-autocomplete/', views.CategoryAutocomplete.as_view(), name='category-autocomplete'),
]
