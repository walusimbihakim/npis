from app.models.inspection import CheckList, CompanyInspection, InspectionCheckList

def get_company_inspections(company):
    return CompanyInspection.objects.filter(company=company)


def get_inspection_fields():
    return CompanyInspection.objects.all()


def get_inspection_field(inspection_id):
    return CompanyInspection.objects.get(pk=inspection_id)


def generate_auto_checklist():
    nspection_count = CompanyInspection.objects.all().count()

    return f"{(nspection_count+1):04}"
