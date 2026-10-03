from django.db import models

Rating_choice = [
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]
# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    imageURL = models.URLField()
    price = models.CharField(max_length=255)
    rating = models.FloatField(choices=Rating_choice)
