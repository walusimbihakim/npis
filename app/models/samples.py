from django.db import models
from django.urls import reverse

from .company import Company

class SampleRequest(models.Model):

    reg_no = models.CharField(max_length=50, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now=False, auto_now_add=False)
    representative = models.CharField(max_length=50)
    report_date = models.CharField(("Expected Report Date"), max_length=50)
    remarks = models.TextField()


    class Meta:
        verbose_name = ("SampleRequest")
        verbose_name_plural = ("SampleRequests")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("SampleRequest_detail", kwargs={"pk": self.pk})


class Sample(models.Model):

    FUEL_TYPE_COICES =[
        ('GS', 'PMS(Gasoline)'),
        ('DS', 'AGO(Diesel)'),
        ('KS', 'BIK(Keresone)'),
        ('EO', 'Engine Oil'),
        ('JF', 'Jet Fuel'),
        ('FO', 'Furnance Oil'),
    ]
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_COICES)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = ("Sample")
        verbose_name_plural = ("Samples")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Sample_detail", kwargs={"pk": self.pk})

