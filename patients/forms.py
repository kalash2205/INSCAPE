from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Patient, Tests, Meds, Bills
from django.db import models



class customform(UserCreationForm):
    # address= models.CharField(max_length=200)
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }
                
    def __init__(self, *args, **kwargs):
        super(customform, self).__init__(*args, **kwargs) 
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})   
            
            
            
class patientform(ModelForm):
    class Meta:
        model= Patient
        fields='__all__'
        exclude= ('user',)
               
    def __init__(self, *args, **kwargs):
        super(patientform, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})    
            
            
class medform(ModelForm):
    class Meta:
        model = Meds
        fields = ['mname']
        # exclude = ('owner', 'mcost')

    def __init__(self, *args, **kwargs):
        super(medform, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})    
                        
                                  
                                  
class testform(ModelForm):
    class Meta:
        model = Tests
        fields = ['tname']
        # exclude = ('owner', 'tcost')

    def __init__(self, *args, **kwargs):
        super(testform, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})    
            
            
class billform(ModelForm):
    class Meta:
        model = Bills
        fields = ['btcost', 'bmcost']
        # exclude = ('owner', 'tcost')

    def __init__(self, *args, **kwargs):
        super(billform, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})                
                        
                                                                    