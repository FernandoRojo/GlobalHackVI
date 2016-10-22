from django import forms

class ShelterForm(forms.Form):
    Name = forms.CharField(label='Your name', max_length=150)
    Description = forms.CharField(label = '(Optional) Description to help others know your shelter',required = False,widget=forms.Textarea)
    Contact = forms.CharField(label='Contact Number',max_length=13)
    ContactE = forms.EmailField(label='Contact Email',max_length=100)
    Address = forms.CharField(label='Address', max_length=200)
    ZipCode = forms.IntegerField(label='ZipCode')
    Food_Av = forms.BooleanField('Food')
    Shelter_Av = forms.BooleanField('Shelter')
    Hygeine_Av = forms.BooleanField('Hygenics')
    Counseling_Av = forms.BooleanField('Counseling')
    Other_Av = forms.BooleanField('Other')
    other = forms.CharField(label='Other Useful Information',required = False)
