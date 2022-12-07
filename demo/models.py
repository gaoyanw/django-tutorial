from django.db import models

# Create your models here.
# create a model, a class represent a table in database
class Book(models.Model):
    # a field will be a column in database
    title = models.CharField(max_length=36, blank=True, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits = 2, decimal_places=2)
    is_published = models.BooleanField(default=False)
    published = models.DateField(blank=True,  null=True, default=None)
    cover = models.FileField(upload_to='covers/', blank=True)