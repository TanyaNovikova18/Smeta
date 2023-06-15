from django.urls import path
from . import views


urlpatterns = [
    path('', views.createBase_home, name='createBase_home'),
    path('materialSelection', views.materialSelection, name='materialSelection'),
]