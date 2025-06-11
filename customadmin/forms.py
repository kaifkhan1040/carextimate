from django import forms
from users.models import CustomUser
from django.forms import EmailInput
from django.forms import ModelForm, TextInput, EmailInput, CharField, PasswordInput, ChoiceField, BooleanField, \
    NumberInput, DateInput
from .models import CarCompany,CarModel,Trim,ServiceCategory,ServiceItem,TrimServicePrice,Country,Tyre
    
class CarCompanyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['country'].widget.attrs.update({'class': 'form-control valid'})
        
        
    class Meta:
            model = CarCompany
            fields = ('name','country',)

class CountryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['code'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['symbole'].widget.attrs.update({'class': 'form-control valid'})
    class Meta:
        model = Country
        fields = ['name', 'code','symbole']

class TyreForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['company'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['model'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['trim'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['country'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['width'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['profile'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['rim'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['load'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['speed'].widget.attrs.update({'class': 'form-control valid'})
    class Meta:
        model = Tyre
        fields = ['name', 'company','model','trim','country',
                  'width','profile','rim','load','speed']
            
class CarModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['company'].widget.attrs.update({'class': 'form-control valid'})
        
    class Meta:
            model = CarModel
            fields = ['name','company']
            
class TrimForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['company'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['model'].widget.attrs.update({'class': 'form-control valid'})
    class Meta:
            model = Trim
            fields = ['name','company','model']
            
class ServiceCategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['image'].widget.attrs.update({'class': 'form-control valid'})
        
    class Meta:
            model = ServiceCategory
            fields = ['name','image']
            
class ServiceItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['category'].widget.attrs.update({'class': 'form-control valid'})
        
    class Meta:
            model = ServiceItem
            fields = ['name','category']