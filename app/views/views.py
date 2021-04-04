from django.shortcuts import render,redirect,reverse
from django.views.generic import DetailView,ListView,UpdateView,CreateView,DeleteView
from app.models.samples import Sample
from app.models.samples import Sample,SampleRequest
from app.forms.sample_form import SampleForm
from app.forms.company_form import CompanyForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# from cuniculture_app.forms.farm_forms import FarmForm
# from cuniculture_app.selectors.farms_selectors import get_farms, get_farm
from app.selectors.sample_selector import get_samples
from app.selectors.company_selector import get_companys,get_company

def index_page_view(request):
    return render(request, "login.html")

def index_page(request):
    return render(request, "index.html")

# Create your views here.
# class IndexView(ListView):
#     template_name="quality_assurance/sample_registration.html"
#     context_object_name = "sample_request_view"
#     model = Sample
    
# class IndexViews(ListView):
#     template_name="quality_assurance/sample_registration.html"
#     context_object_name = "Request_sample_view"
#     model = SampleRequest


# class Sample_RequestCreateView(CreateView):
#     template_name = 'QA/sample_registration.html'
#     form_class = SampleForm
#     queryset = SampleRequest.objects.all()
    # def __init__(self, *args):
    #     super(Sample_RequestCreateView, self).__init__(*args))
        
def manage_sample(request):
    
    sample_form = SampleForm()
    samples = get_samples()
    
    if request.method == "POST":
        sample_form = SampleForm(request.POST, request.FILES)
        if sample_form.is_valid():
            sample_form.save()
            messages.success(request, 'Sample Record saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
         
    context = {
        "sample_form": sample_form,
        "samples": samples
    }
    return render(request, "quality_assurance/sample_registration.html", context)

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
# def delete_pat(request,  id):
#     if request.method=='POST':
#         pi = Patient.objects.get(pk=id)
#         pi.delete()
#     return HttpResponseRedirect('/')

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
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index_page')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    
    else:
        return render (request,'login.html')  

def logout(request):
    auth.logout(request)
    return redirect('/')




    
    
        
    




  
