from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput, DateInput
from django import forms


from app.models.enforcement_field import Field_enforcement

# class InspectionForm(ModelForm):
#     class Meta:
#         model = Inspection
        
#         fields = fields = '__all__'
     
#     def __init__(self, *args, **kwargs):
#         super(InspectionForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()


class EnforcementFieldForm(ModelForm):

    class Meta:
        model = Field_enforcement

        fields = fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
            
        }

    def __init__(self, *args, **kwargs):
        super(EnforcementFieldForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['serial_number'].widget.attrs['readonly'] = True
        # self.fields["serial_number"].widget = HiddenInput()
