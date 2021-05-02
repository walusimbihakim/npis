from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput,DateInput
from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from app.models.company import Company,Products



class CompanyForm(ModelForm):

   
    class Meta:
        model = Company
        
        fields = fields = '__all__'
     
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class ProductForm(ModelForm):

    class Meta:
        model = Products

        fields = fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        

        
