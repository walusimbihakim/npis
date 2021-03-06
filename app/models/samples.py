from django.db import models
from django.urls import reverse

from .company import Company

class SampleRequest(models.Model):

    id = models.AutoField(primary_key=True)

    reg_no = models.CharField("Request No.", max_length=50, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    registration_date = models.DateField(null = True)
    representative = models.CharField(max_length=50)
    report_date = models.CharField(("Expected Report Date"), max_length=50)
    remarks = models.TextField()


    class Meta:
        verbose_name = ("SampleRequest")
        verbose_name_plural = ("SampleRequests")

    def __str__(self):
        return self.reg_no

    def get_absolute_url(self):
        return reverse("SampleRequest_detail", kwargs={"pk": self.pk})


class Sample(models.Model):
    id = models.AutoField(primary_key=True)

    FUEL_TYPE_COICES =[
        ('PMS(Gasoline)', 'PMS(Gasoline)'),
        ('DS', 'AGO(Diesel)'),
        ('KS', 'BIK(Keresone)'),
        ('EO', 'Engine Oil'),
        ('JF', 'Jet Fuel'),
        ('FO', 'Furnance Oil'),
    ]
    para =[
        ('Mk', 'Marker'),
        ('DS', 'Density'),
        ('Qu', 'Quality'),
    ]
    sample_request = models.ForeignKey(SampleRequest, on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=50,choices= FUEL_TYPE_COICES)
    parameter = models.CharField(max_length=20,choices= para)
    type_method = models.CharField(max_length=10)
    test_method = models.CharField(max_length=10)
    unit_fee = models.IntegerField()
    quantity = models.IntegerField(verbose_name="Quantity(mls)")
    

    class Meta:
        verbose_name = ("Sample")
        verbose_name_plural = ("Samples")
        
        unique_together=[("sample_request", "fuel_type")]

    def __str__(self):
        return {self.fuel_type}

    @property
    def total_cost(self):
        total_cost=self.unit_fee*self.quantity

        return total_cost

    def get_absolute_url(self):
        return reverse("Sample_detail", kwargs={"pk": self.pk})

