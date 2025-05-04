from django.shortcuts import render
import logging
from dal import autocomplete
from .models import Subcategory, Category
logger = logging.getLogger('cash_tracker')

class SubcategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Subcategory.objects.all().order_by('name')
        logger.info("SubcategoryAutocomplete: Запрос получен.")
        category_id = self.forwarded.get('category', None)
        logger.info(f"category_id: {category_id}")
        if category_id:
            try:
                logger.info(f"SubcategoryAutocomplete: Передан category_id = {category_id}")
                category = Category.objects.get(id=category_id)

                logger.info(f"SubcategoryAutocomplete: Категория найдена - {category.name}")

                qs = category.subcategories.all()
            except Category.DoesNotExist:
                logger.error(f"SubcategoryAutocomplete: Категория с id {category_id} не найдена.")
                qs = Subcategory.objects.none()

        logger.info(f"SubcategoryAutocomplete: Подкатегорий найдено - {qs.count()}")
        return qs


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Category.objects.all().order_by('name')
        type_id = self.forwarded.get('type', None)
        logger.info("CategoryAutocomplete: Запрос получен.")
        logger.info(f"CategoryAutocomplete: type_id = {type_id}")
        if type_id:
            qs = qs.filter(type_id=type_id)
            logger.info(f"CategoryAutocomplete: Найдено категорий с type_id={type_id} , кол-во: {qs.count()}")
        return qs
