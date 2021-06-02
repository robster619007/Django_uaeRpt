from django.db import models

# Create your models here.
class clients(models.Model):
    client_code = models.IntegerField(primary_key=True)
    client_description = models.CharField(max_length = 150)
    region_code = models.CharField(max_length = 3,default='DXB')
    city_code = models.CharField(max_length = 3)
    subchannel = models.CharField(max_length = 15 )
    channel = models.CharField(max_length = 15)
    Area_of_business = models.CharField(max_length = 3)
    address = models.TextField()
    alt_address = models.TextField()
    email = models.EmailField()
    class Meta:
        verbose_name_plural = "clients"
