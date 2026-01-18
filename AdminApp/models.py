from django.db import models

# Create your models here.

class CategoryDB(models.Model):
    CategoryName = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Category_Image = models.ImageField(upload_to="Profile", null=True, blank=True)


class ProductDB(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Product_Image = models.ImageField(upload_to="Product Image", null=True, blank=True)

