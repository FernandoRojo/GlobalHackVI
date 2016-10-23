from django import forms

class ShelterForm(forms.Form):
    Name = forms.CharField(label='Name of Your Organization', max_length=150)
    Description = forms.CharField(label = '(Optional) Description to help others know your shelter',required = False,widget=forms.Textarea)
    Contact = forms.CharField(label='Contact Number',max_length=13)
    ContactE = forms.EmailField(label='Contact Email',max_length=100)
    Address = forms.CharField(label='Address (be as accurate as possible)', max_length=200)
    foodAvailable = forms.BooleanField(label='Food Available', required = False)
    shelterAvailable = forms.BooleanField(label='Shelter Available', required = False)
    maxCap = forms.IntegerField(label="Maximum Capacity", required = False)
    currCap = forms.IntegerField(label="Current Capacity", required = False)
    hygenicAvailable = forms.BooleanField(label='Hygenic Supplies Available', required = False)
    counselingAvailable = forms.BooleanField(label='Counseling Available', required = False)
    otherDetails = forms.CharField(label='Other Useful Information/Available resources', required = False, widget=forms.Textarea)
    ReferralCode = forms.CharField(label='Referral Code',max_length=13)
