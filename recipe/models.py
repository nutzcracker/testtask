from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=20)
    products = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name
