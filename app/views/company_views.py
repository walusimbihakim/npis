from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from app.forms.company_form import (CompanyForm, ProductForm,
 BranchForm,PermitForm,EmployeeForm,SuplierForm,GasForm
)
from app.selectors.company_selector import (get_companys,
get_company,get_product,get_company_products
,get_company_branches
,get_company_permits
,get_company_employee,get_company_gas,
get_company_supliers,get_company_attachment)

def manage_company(request):
    
    company_form = CompanyForm()
    companys = get_companys()
    
    if request.method == "POST":
        company_form = CompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            company_form.save()
            messages.success(request, 'Company Record saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
         
    context = {
        "company_form": company_form,
        "companys": companys
    }
    return render(request, "company/company_registration.html", context)


def manage_product(request,company_id):
    
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)

        if product_form.is_valid():
           product_form.save()
           messages.success(request,'Product saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
    return HttpResponseRedirect(reverse(company_detail_view, args=[company_id]))


def manage_branch(request, company_id):

    if request.method == "POST":
        branch_form = BranchForm(request.POST, request.FILES)

        if branch_form.is_valid():
           branch_form.save()
           messages.success(request, 'Branch saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
    return HttpResponseRedirect(reverse(company_detail_view, args=[company_id]))


def manage_employee(request, company_id):

    if request.method == "POST":
        employee_form = EmployeeForm(request.POST, request.FILES)

        if employee_form.is_valid():
           employee_form.save()
           messages.success(request, 'Employee saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
    return HttpResponseRedirect(reverse(company_detail_view, args=[company_id]))
    

def manage_permit(request, company_id):

    if request.method == "POST":
        permit_form = PermitForm(request.POST, request.FILES)

        if permit_form.is_valid():
           permit_form.save()
           messages.success(request, 'Permit saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
    return HttpResponseRedirect(reverse(company_detail_view, args=[company_id]))


def manage_supplier(request, company_id):

    if request.method == "POST":
        supplier_form = SuplierForm(request.POST, request.FILES)

        if supplier_form.is_valid():
           supplier_form.save()
           messages.success(request, 'Supplier saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
    return HttpResponseRedirect(reverse(company_detail_view, args=[company_id]))


def manage_gas(request, company_id):

    if request.method == "POST":
        gas_form = GasForm(request.POST, request.FILES)

        if gas_form.is_valid():
           gas_form.save()
           messages.success(request, 'Gas saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
    return HttpResponseRedirect(reverse(company_detail_view, args=[company_id]))

    

def edit_company_view(request, company_id):
    
    company = get_company(id)
    company_form = CompanyForm(instance=company)

    if request.method == "POST":
        company_form = CompanyForm(request.POST, request.FILES, instance=company)

        if company_form.is_valid():
            company_form.save()
            messages.success(request, 'Changes saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
        
        return HttpResponseRedirect(reverse(manage_company))
            
    context = {
        "company_form": company_form,
        "company": company
     }
        
    return render(request, "company/company_edit.html", context)


def company_detail_view(request, company_id):
    company = get_company(company_id)
    company_branch = get_company_branches(company)
    company_products = get_company_products(company)
    company_permit = get_company_permits(company)
    company_employee = get_company_employee(company)
    company_supplier = get_company_supliers(company)
    company_gas = get_company_gas(company)
    company_attachment = get_company_attachment(company)

    product_form = ProductForm(initial={"company": company})
    branch_form = BranchForm(initial={"company": company})
    permit_form = PermitForm(initial={"company": company})
    employee_form = EmployeeForm(initial={"company": company})
    supplier_form = SuplierForm(initial={"company": company})
    gas_form = GasForm(initial={"company": company})
    

    context = {
        "company": company,
        "branches": company_branch,
        "products": company_products,
        "permit": company_permit,
        "supplier": company_supplier,
        "employee": company_employee,
        "gas": company_gas,
        "attachment": company_attachment,
        "product_form": product_form,
        "branch_form": branch_form,
        "permit_form": permit_form,
        "employee_form": employee_form,
        "supplier_form": supplier_form,
        "gas_form": gas_form
    }
    return render(request, "company/company_details.html", context)

def delete_company_view(request, company_id):
    company = get_company(company_id)

    company.delete()
    messages.success(request, 'Company Deleted Successful')
        
    return HttpResponseRedirect(reverse(manage_company))
