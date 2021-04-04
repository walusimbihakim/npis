from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput,DateInput
from app.models.company import  Company
from django import forms
from bootstrap_datepicker_plus import DatePickerInput



# class DateInput(forms.DateInput):
#         input_type = 'date'

class CompanyForm(ModelForm):

    # class DateInput(forms.DateInput):
    #     input_type = 'date'
    
    
    
    class Meta:
        model = Company
        
        
        # registration_date = forms.DateField(
        # widget=forms.TextInput(
        #         attrs={'type': 'date'}
        #     )
        # )
        fields = fields = '__all__'
        # close_date = DateField(input_formats=['%m/%d/%Y'], label=_('Installation Date'),widget=DateInput())
        # widgets = {
        #     'registration_date ': DateInput(attrs={'type': 'date'}),}

       
        
       
        # widgets= {
        #     # 'patient_name'  : forms.TextInput(attrs={'class':'form-control'}),
        #     # 'patient_code' : forms.TextInput(attrs={'class':'form-control'}),
        #     # 'complain'  : forms.TextInput(attrs={'class':'form-control'}),
        #     # # 'gender'  : forms.TextInput(attrs={'class':'form-control'}),
        #     'registration_date': DateInput(attrs={'type': 'date'}),
        # }
        
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        

        