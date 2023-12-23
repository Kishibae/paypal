from django.db import models

class Book(models.Model):
    bid = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
