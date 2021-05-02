from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput,DateInput
from app.models.samples import  Sample,SampleRequest

class SampleRequestForm(ModelForm):

    class Meta:
        model = SampleRequest
                
        fields = fields = '__all__'
        widgets = {
           'registration_date': DateInput(attrs={'type': 'date'}), 
           'report_date': DateInput(attrs={'type': 'date'})
        }  
          
    def __init__(self, *args, **kwargs):
        super(SampleRequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

class SampleForm(ModelForm):
        
    class Meta:
        model = Sample
                
        fields = fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(SampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.fields["sample_request"].widget = HiddenInput()
        