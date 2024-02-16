from django.db import models

# Create your models here.
class Tenant(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    tenant_name = models.CharField(max_length = 255)
    lot_number = models.IntegerField()
  
class Place(models.Model):
    place = models.CharField(max_length = 255)
    
# # class Lessor(models.Model):  
#     lessor_name = models.CharField(max_length = 255)
#     place = models.CharField(max_length = 255)

class LessorName(models.Model):
    lessor_name = models.CharField(max_length = 255)
    # place = models.ForeignKey(Place, on_delete=models.CASCADE)


class Treaty(models.Model):
    treaty_date = models.DateField()
    treaty_number = models.CharField(max_length = 255)
    treaty_type = models.CharField(max_length = 255)