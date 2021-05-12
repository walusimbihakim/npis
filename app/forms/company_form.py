from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput,DateInput
from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from app.models.company import (Company,Products,
Branches,Permits,Employees,Attachments,Gas,Suppliers)




class CompanyForm(ModelForm):




   
    class Meta:
        model = Company
        
        fields = fields = ['name', 'contact_no',
                           'address', 'district', 'county', 'sub_county', 'parish', 'village', 'ownership']
     
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


class BranchForm(ModelForm):

    class Meta:
        model = Branches

        fields = fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BranchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class PermitForm(ModelForm):

    class Meta:
        model = Permits

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PermitForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class EmployeeForm(ModelForm):

    class Meta:
        model = Employees

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class SuplierForm(ModelForm):

    class Meta:
        model = Suppliers

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SuplierForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class GasForm(ModelForm):

    class Meta:
        model = Gas

        fields = fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GasForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class AttachmentForm(ModelForm):

    class Meta:
        model = Attachments

        fields = fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AttachmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        

        
