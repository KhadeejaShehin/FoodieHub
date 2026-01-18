from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

class RegistrationDb(models.Model):
    UserName = models.CharField(max_length=100, null=True, blank=True)
    Password1 = models.CharField(max_length=100, null=True, blank=True)
    Password2 = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)


class CartDb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)
    Prod_Image = models.ImageField(upload_to="Cart Images",null=True, blank=True)

class OrderDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Pincode = models.IntegerField(null=True, blank=True)
    TotalPrice = models.IntegerField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)
