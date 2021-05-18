from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
import datetime


from app.models.inspection import CheckList, CompanyInspection, InspectionCheckList
from app.forms.inspection_forms import CheckListForm, CompanyInspectionForm, InspectionCheckListForm
from app.selectors.company_selector import get_company
from app.selectors.inspection_selectors import get_company_inspections, generate_auto_checklist


def manage_company_inspection(request, company_id):
    company = get_company(company_id)
    auto_checklist = generate_auto_checklist()
    year = datetime.datetime.today().year
    inspection_no = f"MEMD/INSP/CL/{year}/{auto_checklist}"
    

    company_inspection_form = CompanyInspectionForm(
        initial={"inspection_no": inspection_no,"company":company})

    if request.method == "POST":
        company_inspection_form = CompanyInspectionForm(request.POST, request.FILES)

        if company_inspection_form.is_valid():
            company_inspection_form.save()

            messages.success(request, 'Company Inspection record saved')
    
        else:
            messages.error(request, 'Failed to save data, chck your input and try again')
    
    
    company_inspections = get_company_inspections(company)

    context = {
        'company': company,
        'inspection_form': company_inspection_form,
        'inspections': company_inspections,
    }

    return render(request, 'inspection/company_inspection.html', context)
