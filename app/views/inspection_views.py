from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
import datetime


from app.models.inspection import CheckList, CompanyInspection, InspectionCheckList
from app.forms.inspection_forms import CheckListForm, CompanyInspectionForm, InspectionCheckListForm
from app.selectors.company_selector import get_company
import app.selectors.inspection_selectors as inspection_selectors
 


def manage_company_inspection(request, company_id):
    auto_checklist = inspection_selectors.generate_auto_checklist()
    year = datetime.datetime.today().year
    inspection_no = f"MEMD/INSP/CL/{year}/{auto_checklist}"
    

    company_inspection_form = CompanyInspectionForm(
        initial={"inspection_no": inspection_no})

    if request.method == "POST":
        company_inspection_form = CompanyInspectionForm(request.POST, request.FILES)

        if company_inspection_form.is_valid():
            company_inspection_form.save()

            checklists = inspection_selectors.get_checklists()

            inspection = inspection_selectors.get_current_inspection()

            for item in checklists:
                inspection_checklist = InspectionCheckList(
                    inspection = inspection,
                    checklist = item,                    
                    )
                
                inspection_checklist.save()

            messages.success(request, 'Company Inspection record saved')
    
        else:
            messages.error(request, 'Failed to save data, chck your input and try again')
    
    company = get_company(company_id)
    company_inspections = inspection_selectors.get_company_inspections(company)

    context = {
        'company': company,
        'inspection_form': company_inspection_form,
        'inspections': company_inspections,
    }

    return render(request, 'inspection/company_inspection.html', context)

def manage_inspection_checklist(request, inspection_id):
    inspection = inspection_selectors.get_inspection(inspection_id)

    if request.method == "POST":
        status = request.POST.get('status')
        remarks = request.POST.get('remarks')
        checklist_id = request.POST.get('checklist')

        checklist_item = inspection_selectors.get_inspection_checklist_item(checklist_id)

        checklist_item.status = status
        checklist_item.remarks = remarks
        checklist_item.is_responded_to = True

        checklist_item.save()

        messages.success(request, 'Checklist Item saved')

    inspection_checklist = inspection_selectors.get_company_inspection_checklist(inspection)
    next_checklist_item = inspection_selectors.get_next_checklist_item(inspection)
    
    print(inspection_checklist)
    context = {
        'inspection': inspection,
        'checklist_items': inspection_checklist,
        'next_checklist_item': next_checklist_item,
    }
    return render(request, 'inspection/inspection_checklist.html', context)
