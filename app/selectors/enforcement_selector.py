from app.models.enforcement_field import Field_enforcement,Inspection


def get_enforcement_fields():
    return Field_enforcement.objects.all()


def get_enforcement_field(field_id):
    return Field_enforcement.objects.get(pk=field_id)


def generate_auto_serialnumber():
    request_count = Field_enforcement.objects.all().count()

    return f"{(request_count+1):04}"


def get_inspection_fields():
    return Inspection.objects.all()


def get_inspection_field(inspection_id):
    return Inspection.objects.get(pk=inspection_id)


def generate_auto_checklist():
    request_count = Inspection.objects.all().count()

    return f"{(request_count+1):04}"
