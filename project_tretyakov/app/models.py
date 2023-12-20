from django.db import models

# Create your models here.
class Dishes(models.Model):
    name = models.CharField(max_length=50)
    # category = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.CharField(max_length=50)
    ingredients = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name_category = models.CharField(max_length=50)

    def __str__(self):
        return self.name_category