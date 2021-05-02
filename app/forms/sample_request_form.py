from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput,DateInput
from app.models.samples import  Sample,SampleRequest
from django import forms
from bootstrap_datepicker_plus import DatePickerInput

class Sample_request_form(ModelForm):
    
    class Meta:
        model = SampleRequest
                
        fields = fields = '__all__'
        widgets = {
           'registration_date': DateInput(attrs={'type': 'date'}), 
           'report_date': DateInput(attrs={'type': 'date'})
        }  
        
    def __init__(self, *args, **kwargs):
        super(SampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        
        