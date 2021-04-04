from app.models.company import Company

def get_companys():
    return Company.objects.all()

def get_company(id):
    return Company.objects.get(pk=id)