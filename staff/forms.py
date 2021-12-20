from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import  Department, Staff



# class customform(UserCreationForm):
#     class Meta:
#         model = User
#         fields = []
              
        
#     def __init__(self, *args, **kwargs):
#         super(customform, self).__init__(*args, **kwargs) 
        
#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'input'}) 
            


class staff_form(ModelForm):
    class Meta:
        model= Staff
        fields='__all__'
        exclude=('user', )
        
        
    def __init__(self, *args, **kwargs):
        super(staff_form, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})    
                      