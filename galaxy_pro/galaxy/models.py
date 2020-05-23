from django.db import models
import datetime

# Create your models here.
class Servers(models.Model):
    Instancename=models.CharField(max_length = 15 , unique= True)
    ip=models.GenericIPAddressField(protocol='both',unpack_ipv4=False,unique=True)
    port=models.PositiveIntegerField(default=22)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    OsType=models.CharField(max_length=50 , default='unknown')

    def __str__(self):
        return self.Instancename


class Request(models.Model):
    Instancename=models.CharField(max_length = 15)
    ip=models.GenericIPAddressField(protocol='both',unpack_ipv4=False)
    status=models.CharField(max_length=10)
    request=models.CharField(max_length=10)
    requesttime=models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.Instancename
