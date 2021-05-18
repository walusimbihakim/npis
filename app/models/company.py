from django.db import models
from django.urls import reverse

import datetime


# Create your models here.

class Company(models.Model):    
    FACILTY_TYPE_CHOICES = [
        ('Depot', 'Depot'),
        ('Truck', 'Truck'),
        ('Service', 'Service'),
        ('Filling Station', 'Filling Station')

    ]
    id = models.AutoField(primary_key=True)
    facility_type = models.CharField(max_length=50,choices=FACILTY_TYPE_CHOICES)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    registration_no = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)
    region = models.CharField(max_length=200)
    district = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    sub_county = models.CharField(max_length=50)
    post_code = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    ownership = models.CharField(max_length=50)
    parish = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    tin = models.CharField(max_length=50)
    logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,null = True,blank=True)
    distance = models.CharField(verbose_name="Distance from Nearest Licensed Station.",max_length=100, null=True)
    
    


    class Meta:
        verbose_name = ("Company")
        verbose_name_plural = ("Companys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Company_detail", kwargs={"pk": self.pk})

class NemaCertifcate(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    certificate_no = models.CharField(max_length=25, verbose_name="NEMA Certificate No.")
    create_date = models.DateField()
    audit_due_date = models.DateField()
    project = models.CharField(max_length=50)
    project_purpose = models.TextField()
    received_date = models.DateField()
    certifcate_one=models.FileField()
    certifcate_two = models.FileField()
    certifcate_three = models.FileField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.certificate_no


class Products(models.Model):    
    id = models.AutoField(primary_key=True)
    PRODUCT_TYPE_CHOICES = [
        ('PMS', 'PMS'),
        ('AGO', 'AGO'),
        ('BIK', 'BIK'),
        ('OTHERS', 'OTHERS')

    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product_type = models.CharField(
        max_length=200, choices=PRODUCT_TYPE_CHOICES)
    tank_details = models.CharField(max_length=200)
    stock = models.CharField(max_length=200)
    product_prices = models.CharField(max_length=150)
    

    def __str__(self):
        return self.product_type

class ProductPrics(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_prices = models.CharField(max_length=150)

    def __str__(self):
        return self.product


class Gas(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    LPG_prices = models.PositiveIntegerField()
    LPG_item = models.CharField(max_length=150)
    LPG_Description = models.CharField(max_length=150)

    def __str__(self):
        return self.LPG_item






class Permits(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    construction_permit = models.CharField(
        verbose_name="Construction Permit Number", max_length=200)
    operation_permit = models.CharField(
        verbose_name="Operating License Number", max_length=200)
    TIN = models.CharField(
        verbose_name="Company Tax identification Number", max_length=200)

    def __str__(self):
        return self.company


class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    female = models.PositiveIntegerField()
    male = models.PositiveIntegerField()

    def __str__(self):
        return self.company


class Suppliers(models.Model):
    
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.company


class Attachments(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    attachment_file = models.FileField(upload_to='attachments')

    def __str__(self):
        return f'{self.company} - {self.name}'


class Branches(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.company
