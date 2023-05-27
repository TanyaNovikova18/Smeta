from django.db import models


class Base(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    Категория = models.CharField(max_length=200)
    Название_продукта = models.CharField(max_length=500)
    Ед_измерения = models.CharField(max_length=50)
    Цена = models.FloatField()

    def __str__(self):
        return self.Категория
