from django.contrib import admin
from django.contrib.admin.decorators import register
from django.shortcuts import render
from django import forms
from .models import *
from django.urls import path

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()
class BaseOne(admin.ModelAdmin):
    list_display = ('id', 'Категория', 'Название_продукта', 'Ед_измерения', 'Цена')
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            file_data = csv_file.read().decode("ANSI")
            csv_data = file_data.split("\r")

            for x in csv_data:
                fields = x.split(";")
                created = Base.objects.update_or_create(
                    id = fields[0],
                    Категория = fields[1],
                    Название_продукта = fields[2],
                    Ед_измерения = fields[3],
                    Цена = fields[4],
                )


        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)
admin.site.register(Base, BaseOne)
