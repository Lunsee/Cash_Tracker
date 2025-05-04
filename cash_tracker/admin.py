from django.contrib import admin
from rangefilter.filters import DateTimeRangeFilter

from .models import Transaction, Type, Category, Subcategory, Status
from django import forms
from dal import autocomplete
# Register your models here.
from .forms import TransactionForm
import logging

logger = logging.getLogger(__name__)

# Админка для транзакций
class TransactionAdmin(admin.ModelAdmin):
    form = TransactionForm
    list_display = ('formatted_date', 'status', 'type', 'category', 'subcategory', 'sum', 'comment')
    list_filter = (
        ('date', DateTimeRangeFilter),
        'status', 'type', 'category', 'subcategory'
    )
    readonly_fields = ('date',)
    search_fields = ('comment', 'status__name', 'type__name', 'category__name', 'subcategory__name')
    list_per_page = 10


    def formatted_date(self, obj):   # Форматирование даты
        return obj.date.strftime('%Y-%m-%d %H:%M:%S')

    formatted_date.short_description = 'Date'


# Админка для статусов
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Админка для типов
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Админка для категорий
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'get_subcategories')
    search_fields = ('name',)
    list_filter = ('type',)
    filter_horizontal = ('subcategories',)

    #метод отображения всех подкатегорий
    def get_subcategories(self, obj):
        return ", ".join([s.name for s in obj.subcategories.all()])
    get_subcategories.short_description = "Subcategories"


# Админка для подкатегорий
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Регистрация моделей
admin.site.register(Status, StatusAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)