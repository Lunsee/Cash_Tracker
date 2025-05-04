from dal import autocomplete
from .models import Transaction, Type, Category, Subcategory, Status
from django import forms

# создание формы для заполнения и привязка эндпоинтов
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {
            'category': autocomplete.ModelSelect2(
                url='category-autocomplete', #эндпоинт
                forward=['type']  # фильтруем категории по типу
            ),
            'subcategory': autocomplete.ModelSelect2(
                url='subcategory-autocomplete',
                forward=['category']
            )
        }




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategories.all()
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type)

