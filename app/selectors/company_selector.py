from app.models.company import Company,Products,Branches

def get_companys():
    return Company.objects.all()

def get_company(id):
    return Company.objects.get(pk=id)


def get_company_products(company):
    return Products.objects.filter(company=company)


def get_company_branches(company):
    return Branches.objects.filter(company=company)


def get_product(product_id):
    return Products.objects.get(pk=product_id)
