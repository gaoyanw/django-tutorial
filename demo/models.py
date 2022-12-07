from django.db import models

# Create your models here.
# create a model, a class represent a table in database
class Book(models.Model):
    # a field will be a column in database
    title = models.CharField(max_length=36)