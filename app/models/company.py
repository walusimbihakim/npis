from django.db import models
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    

    
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    registration_no = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    region = models.CharField(max_length=50)
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



    class Meta:
        verbose_name = ("Company")
        verbose_name_plural = ("Companys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Company_detail", kwargs={"pk": self.pk})
