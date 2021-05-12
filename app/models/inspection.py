from django.db import models
from django.urls import reverse
from app.models.company import Company


class CheckList(models.Model):
    description = models.TextField()

    def __str__(self):
       return self.description


class CompanyInspection(models.Model):
    inspection_no = models.CharField(max_length=25)
    inspection_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    inspector = models.CharField(max_length=50, verbose_name="Inspected By")
    recommendation = models.TextField()


class InspectionCheckList(models.Model):
    company_inspection = models.ForeignKey(
        CompanyInspection, on_delete=models.RESTRICT)
    checkList = models.ForeignKey(
        CheckList, verbose_name="Particular", on_delete=models.RESTRICT)
    status = models.BooleanField()
    remarks = models.TextField()
