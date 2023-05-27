from django.db import models

# Create your models here.
class TypeSelection(models.Model):
    at_this_moment = models.BooleanField("На текущий момент", default=False)
    intermediate = models.BooleanField("Промежуточная", default=False)
    year = (
        ('1', '1 год'),
        ('2', '2 года'),
        ('3', '3 года'),
    )
    years1 = models.CharField(max_length=10, choices=year, default='1')
    delayed = models.BooleanField("Отложенная", default=False)
    years2 = models.CharField(max_length=10, choices=year, default='1')


