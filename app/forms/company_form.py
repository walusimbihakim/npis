from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput,DateInput
from app.models.company import  Company
from django import forms
from bootstrap_datepicker_plus import DatePickerInput



class CompanyForm(ModelForm):

   
    class Meta:
        model = Company
        
        fields = fields = '__all__'
     
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        

        