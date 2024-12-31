from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label='Full Name : ', help_text='Total length must be within 70 characters',required=False,widget=forms.Textarea(attrs={'id' : 'text_area','class' : 'class1 class2', 'placeholder' : 'Enter your name'}))
    # file = forms.FileField()
    email = forms.EmailField(label='User Email')
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appoinment = forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S' , 'Small'),('M' , 'Medium'),('L' , 'Large')]
    size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    MEAL = [('B' , 'Beef'),('C' , 'Chicken'),('M' , 'Mashroom')]
    pizza = forms.MultipleChoiceField(choices = MEAL, widget=forms.CheckboxSelectMultiple)
    
    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError('Enter a name with at least 10 characters')
#     #     return valname
    
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError('Your email must contain .com')
#     #     return valemail
    
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError('Enter a name with at least 10 characters')
#         if '.com' not in valemail:
#             raise forms.ValidationError('Your email must contain .com')

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError('Enter a value at least 10 chars')

class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message='Enter a name with at least 10 characters')])
    text = forms.CharField(widget=forms.TextInput,validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='Enter a valid email')])
    age = forms.IntegerField(validators=[validators.MinValueValidator(10, message='age must be 10'),validators.MaxValueValidator(34,message='age must be maximum 34')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'])])

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_pass != val_conpass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")