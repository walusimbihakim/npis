from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from app.forms.company_form import CompanyForm,ProductForm
from app.selectors.company_selector import (get_companys,
get_company,get_product,get_company_products
,get_company_branches)

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


def manage_product(request):

    product_form = ProductForm()
    products = get_company_products()

    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, 'Product Record saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')

    context = {
        "product_form": product_form,
        "products": products
    }
    return render(request, "company/company_registration.html", context)

def edit_company_view(request, id):
    
    company = get_company(id)
    company_form = CompanyForm(instance=company)

    if request.method == "POST":
        company_form = CompanyForm(request.POST, request.FILES, instance=company)

        if company_form.is_valid():
            company_form.save()
            messages.success(request, 'Changes saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
            
    context = {
        "company_form": company_form,
        "company": company
     }
        
    return render(request, "company/company_edit.html", context)


def company_detail_view(request, id):
    company = get_company(id)
    branch = get_company_branches(company)
    company_products = get_company_products(company)


    context = {
        "company": company,
        "branches": branch,
        "products": company_products
    }
    return render(request, "company/company_details.html", context)

def delete_company_view(request, id):
    company = get_company(id)

    company.delete()
    messages.success(request, 'Company Deleted Successful')
        
    return HttpResponseRedirect(reverse(manage_company))
