from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        # fields = ('fullName', 'mobileNo', 'empCode', 'position')
        fields = '__all__'

        labels = {
            'fullName' : 'Full Name',
            'empCode' : 'EMP.Code',
        }


    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__( *args, **kwargs)
        self.fields['position'].empty_label = "--select--"
        self.fields['empCode'].required = False
