from app.models.inspection import CheckList, CompanyInspection, InspectionCheckList
from django.db.models import Max

def get_checklists():
    return CheckList.objects.all()

def get_company_inspections(company):
    return CompanyInspection.objects.filter(company=company)

def get_inspection(inspection_id):
    return CompanyInspection.objects.get(pk=inspection_id)

def get_company_inspection_checklist(inspection):
    return InspectionCheckList.objects.filter(inspection=inspection, is_responded_to=True)

def get_next_checklist_item(inspection):
    return InspectionCheckList.objects.filter(inspection=inspection, is_responded_to=False).first()

def get_inspection_checklist_item(id):
    return InspectionCheckList.objects.get(pk=id)

def get_current_inspection():
    return CompanyInspection.objects.all().last()

def get_inspection_fields():
    return CompanyInspection.objects.all()


def get_inspection_field(inspection_id):
    return CompanyInspection.objects.get(pk=inspection_id)


def generate_auto_checklist():
    nspection_count = CompanyInspection.objects.aggregate(Max("id"))

    return f"{(nspection_count['id__max']+1):04}"
