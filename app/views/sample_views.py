from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from django.views import View
from django.template.loader import get_template

import datetime
from app.utils import render_to_pdf
from app.models.samples import Sample,SampleRequest
from app.forms.sample_form import SampleRequestForm, SampleForm
from app.selectors.sample_selector import (
    get_sample_requests, 
    get_sample_request,
    get_samples_on_request,
    generate_auto_number,
)

     
def manage_sample_requests(request):
    
    auto_no = generate_auto_number()
    year = datetime.datetime.today().year
    request_no = f"MEMD/LAB/RAF/{year}/{auto_no}"
    
    request_form = SampleRequestForm(initial={"reg_no":request_no})
    requests = get_sample_requests()
    
    if request.method == "POST":
        request_form = SampleRequestForm(request.POST, request.FILES)
        if request_form.is_valid():
            request_form.save()
            messages.success(request, 'Sample Request Record saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
         
    context = {
        "request_form": request_form,
        "requests": requests
    }
    return render(request, "quality_assurance/manage_sample_requests.html", context)

def manage_samples(request, sample_request_id):
    
    sample_request = get_sample_request(sample_request_id)
    
    sample_form = SampleForm(initial={"sample_request":sample_request})
    
    samples = get_samples_on_request(sample_request)
    
    if request.method == "POST":
        sample_form = SampleForm(request.POST, request.FILES)
        
        if sample_form.is_valid():
            sample_form.save()
            messages.success(request, 'Sample Record saved Successfully!')
            
        else:
            messages.warning(request, 'Operation Not Successfull')
            
        return HttpResponseRedirect(reverse(manage_samples,args=[sample_request_id]))
         
    context = {
        "sample_form": sample_form,
        "samples": samples
    }
    return render(request, "quality_assurance/manage_samples.html", context)


def request_details_view(request, sample_request_id):
    sample_request = get_sample_request(sample_request_id)

    samples = get_samples_on_request(sample_request)

    context = {
        "request":sample_request,
        "samples": samples,
    }
    return render(request, "quality_assurance/sample_request_details.html", context)


def generate_pdf(request, sample_request_id):    

    sample_request = get_sample_request(sample_request_id)

    samples = get_samples_on_request(sample_request)

    context = {
        "request": sample_request,
        "samples": samples,
    }
    pdf = render_to_pdf('test.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

# def get(self, request, *args, **kwargs):

#     template = get_template('quality_assurance/sample_request_details.html')
#     data = {
#             'today': datetime.date.today(),
#             'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         # pdf = render_to_pdf('pdf/invoice.html', data)
#         # return HttpResponse(pdf, content_type='application/pdf')
#     html = template.render(data)
#     return HttpResponse(html)
    
    
        
    




  
