from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput, DateInput, widgets
from django import forms


from app.models.inspection import CheckList, CompanyInspection, InspectionCheckList


class CheckListForm(ModelForm):
    class Meta:
        model = CheckList

        fields = fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CheckListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class CompanyInspectionForm(ModelForm):
    class Meta:
        model = CompanyInspection

        fields = '__all__'

        widgets = {
            "inspection_date": DateInput(attrs={'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CompanyInspectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['company'].widget=HiddenInput()
        self.fields['inspection_no'].widget.attrs['readonly'] = True


class InspectionCheckListForm(ModelForm):
    class Meta:
        model = InspectionCheckList

        fields = fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(InspectionCheckListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
