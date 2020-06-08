from django.db import models
from datetime import date
import uuid

# Create your models here.


def upload_to_profile(instance, filename):
    extension = filename.split(".")[-1]
    return "images/profile/%s/%s.%s" % (instance.Staff, uuid.uuid4(), extension)

def upload_to_product(instance, filename):
    extension = filename.split(".")[-1]
    return "images/product/%s/%s.%s" % (instance.Product, uuid.uuid4(), extension)

class Position(models.Model):
    PositionName = models.CharField(max_length=50, null=False)
    def __str__(self):
        return str(self.PositionName)

class Staff(models.Model):
    StaffId = models.CharField(max_length=10, null=False, primary_key=True)
    FullName = models.CharField(max_length=50, null=False)
    DateOfBirth  = models.DateField()
    JoinDate = models.DateField()
    Gender_Choice = [('Male', 'Male'), ('Female', 'Female')]
    Gender = models.CharField(max_length=10, choices=Gender_Choice)
    Image = models.ImageField(upload_to=upload_to_profile)
    Email = models.EmailField(null=True, blank=True)
    Phone = models.CharField(max_length=11, null=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    Position = models.ForeignKey( Position, related_name='Position', on_delete=models.SET_NULL, null=True)
    Status_Choice = [('Enable', 'Enable'), ('Disable', 'Disable')]
    Status = models.CharField(
        max_length=10, choices=Status_Choice, default='Enable')

    def __str__(self):
        return str(self.FullName)

class ProductType(models.Model):
    TypeName = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return str(self.TypeName)

class Product(models.Model):
    ProductName = models.CharField(max_length=50, null=False)
    Image = models.ImageField(upload_to=upload_to_product)
    Price = models.FloatField()
    Type = models.ForeignKey(
        ProductType, related_name='ProductType', on_delete=models.SET_NULL, null=True)

class Invoice(models.Model):
    CreateDate = models.DateTimeField()
