from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('base', views.about, name='base'),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]

