from django.db import models

#https://www.webforefront.com/django/modeldatatypesandvalidation.html
#Creating model for items
class Item(models.Model):

    user_id = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()

    #models.ImageField() potential need pillow (discontined?)
    image = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
