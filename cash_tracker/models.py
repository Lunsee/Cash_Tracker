from django.db import models
import pydantic
import time

#Модель статуса
class Status(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Status"

#Модель Типа
class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

#Модель подкатегорий
class Subcategory(models.Model):
    name = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Subcategories"


#Модель категорий
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(Type, related_name='categories', on_delete=models.CASCADE)  # Привязка категории к типу
    subcategories = models.ManyToManyField('Subcategory', related_name='categories', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


#Модель транзакция
class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    sum = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} | {self.status} | {self.type} | {self.sum} ₽"








