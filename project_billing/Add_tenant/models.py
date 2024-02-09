from django.db import models

# Create your models here.
class Tenant(models.Model):
    place = models.CharField(max_length = 255)
    start_date = models.CharField(max_length = 255)
    end_date = models.CharField(max_length = 255)
    tenant_name = models.CharField(max_length = 255)