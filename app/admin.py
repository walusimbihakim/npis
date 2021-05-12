from django.contrib import admin
from app.models import  Sample,Company,SampleRequest
from app.models.samples import Sample, SampleRequest
from app.models.company import Company, Attachments

from app.models.inspection import CheckList, CompanyInspection, InspectionCheckList

admin.site.register(Company)
admin.site.register(CheckList)
admin.site.register(CompanyInspection)
admin.site.register(Attachments)
admin.site.register(InspectionCheckList)
