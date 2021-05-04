from app.models.company import (Company,Products,
Branches,Permits,Employees,Suppliers,Gas,Attachments)

def get_companys():
    return Company.objects.all()

def get_company(id):
    return Company.objects.get(pk=id)


def get_company_products(company):
    return Products.objects.filter(company=company)


def get_company_branches(company):
    return Branches.objects.filter(company=company)


def get_company_permits(company):
    return Permits.objects.filter(company=company)


def get_company_employee(company):
    return Employees.objects.filter(company=company)


def get_company_supliers(company):
    return Suppliers.objects.filter(company=company)


def get_company_gas(company):
    return Gas.objects.filter(company=company)


def get_company_attachment(company):
    return Attachments.objects.filter(company=company)


def get_product(product_id):
    return Products.objects.get(pk=product_id)
