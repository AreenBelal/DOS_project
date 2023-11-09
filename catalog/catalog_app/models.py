import django.db.models
from django.db import models

# Create your models here.


class Catalog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    count = models.IntegerField(default=0, null=False)
    cost = models.PositiveIntegerField(default=0, null=False)
