from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('name','surname','city','department')
        labels = {
            'name':'Name',
            'surname': 'Surname',
            'city':'City'
            # 'student_code':'STU. Code'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Select"
        # self.fields['student_code'].required = False