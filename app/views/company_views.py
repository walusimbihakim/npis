from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from app.forms.company_form import CompanyForm
from app.selectors.company_selector import get_companys,get_company

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

def edit_company_view(request, id):
    
    company = get_company(id)
    company_form = CompanyForm(instance=company)

    if request.method == "POST":
        company_form = CompanyForm(request.POST, request.FILES)

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

def delete_company_view(request, id):
    company = get_company(id)

    company.delete()
    messages.success(request, 'Company Deleted Successful')
        
    return HttpResponseRedirect(reverse(manage_company))