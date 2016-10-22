from django import forms

class ShelterForm(forms.Form):
    Name = forms.CharField(label='Your name', max_length=150)
    Description = forms.CharField(label = '(Optional) Description to help others know your shelter',required = False,widget=forms.Textarea)
    Contact = forms.CharField(label='Contact Number',max_length=13)
    ContactE = forms.EmailField(label='Contact Email',max_length=100)
    Address = forms.CharField(label='Address', max_length=200)
    foodAvailable = forms.BooleanField(label='Food Available', required = False)
    shelterAvailable = forms.BooleanField(label='Shelter Available', required = False)
    hygenicAvailable = forms.BooleanField(label='Hygenics Available', required = False)
    counselingAvailable = forms.BooleanField(label='Counseling Available', required = False)
    otherAvailable = forms.BooleanField(label='Other Reasources', required = False)
    other = forms.CharField(label='Other Useful Information', required = False)
