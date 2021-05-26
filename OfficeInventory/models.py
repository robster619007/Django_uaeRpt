from django.db import models
# Create your models here.

class OfficeInventory(models.Model):
    _id = models.BigAutoField(primary_key=True)
    inv_name = models.CharField(max_length = 200)
