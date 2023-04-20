from django.db import models

# Create your models here.
class enquiry(models.Model):
    
    id               = models.AutoField(primary_key=True)
    name             = models.CharField(max_length=100)
    email            = models.EmailField(max_length=300)
    phone            = models.CharField(max_length=10)
    message          = models.CharField(max_length=2000)

    class Meta:
        db_table='enquiry'