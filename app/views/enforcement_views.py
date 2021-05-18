from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse

import datetime

from app.utils import render_to_pdf
from app.forms.enforcement_field_form import EnforcementFieldForm
from app.selectors.enforcement_selector import (get_enforcement_field,
 get_enforcement_fields,generate_auto_serialnumber
 
)

# def manage_inspection_field(request):
#     auto_checklist=generate_auto_checklist()
#     year = datetime.datetime.today().year
#     request_checklist_number = f"MEMD/INSP/CL/{year}/{auto_checklist}"
#     inspection_field_form = InspectionForm(
#         initial={"checklist No": request_checklist_number})
#     inspection_field_forms = get_inspection_fields()

#     if request.method == "POST":
#         inspection_field_form = InspectionForm(request.POST, request.FILES)
#         if inspection_field_form.is_valid():
#             inspection_field_form.save()
#             messages.success(request, 'inspection Record saved Successfully!')

#         else:
#             messages.warning(request, 'Operation Not Successfull')


#     context = {
#         "inspection_field_form": inspection_field_form,
#         "inspection_field_forms": inspection_field_forms
#     }
#     return render(request, "enforcement/inspection_field.html", context)

def manage_enforcement_field(request):

    auto_no = generate_auto_serialnumber()
    year = datetime.datetime.today().year
    request_serial_number = f"MEMD/INSP/CL/{year}/{auto_no}"

    enforcement_field_form = EnforcementFieldForm(
        initial={"serial_number": request_serial_number})
    enforcement_field_forms = get_enforcement_fields()

    if request.method == "POST":
        enforcement_field_form = EnforcementFieldForm(request.POST, request.FILES)
        if enforcement_field_form.is_valid():
            enforcement_field_form.save()
            messages.success(request, 'enforcement Record saved Successfully!')

        else:
            messages.warning(request, 'Operation Not Successfull')

        return HttpResponseRedirect(reverse(manage_enforcement_field))

    context = {
        "enforcement_field_form": enforcement_field_form,
        "enforcement_field_forms": enforcement_field_forms
    }
    return render(request, "enforcement/enforcement_field.html", context)


def edit_field_view(request, field_id):

    field = get_enforcement_field(field_id)
    enforcement_field_form = EnforcementFieldForm(instance=field)

    if request.method == "POST":
        enforcement_field_form = EnforcementFieldForm(
            request.POST, request.FILES, instance=field)

        if enforcement_field_form.is_valid():
            enforcement_field_form.save()
            messages.success(request, 'Changes saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
        return HttpResponseRedirect(reverse(manage_enforcement_field))

    context = {
        "enforcement_field_form": enforcement_field_form,
        "field": field
    }

    return render(request, "enforcement/enforcement_field_edit.html", context)


def request_details_field_view(request, field_id):
    field_request = get_enforcement_field(field_id)

    context = {
       
        "field_request": field_request
    }
    return render(request, "enforcement/field_enforcment_detail.html", context)


def print_enforcement_field(request, field_id):

    field_request = get_enforcement_field(field_id)

    context = {
        "field_request": field_request
    }
    pdf = render_to_pdf('enforcement/reports/field_enforcment_detail_report.html', context)
    return HttpResponse(pdf, content_type='application/pdf')
