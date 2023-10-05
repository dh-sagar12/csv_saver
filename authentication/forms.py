from django import forms

from authentication.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'block w-full px-4 py-2 mt-2 text-black bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40'


    email  =  forms.EmailField(max_length=100, required=True)
    first_name = forms.CharField(label='first_name', max_length=50, required=True)
    middle_name = forms.CharField(label='Middle Name',  max_length=50, required=False)
    last_name = forms.CharField( label='Last Name',  max_length=50, required=True)

    date_of_birth = forms.DateField(widget=forms.DateInput({'type': 'date'}), required=True)
    
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'), (GENDER_OTHER, 'Other')]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    
    class Meta:
        model  =  User
        fields  =  ['email', 'first_name', 'middle_name', 'last_name']
        labels  =  {
            'email': "email"
        }
        widgets= {
            'email': forms.EmailInput(attrs= {'placeholder': 'Enter your valid email address', }),
            'first_name': forms.TextInput(attrs= {'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs= {'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs= {'placeholder': 'Last Name'}),
        }