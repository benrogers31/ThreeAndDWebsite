from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Account


#this class inherits from Django's prebuilt user creation form
class UserRegisterForm(UserCreationForm):
    #generates an email field default is required=true
    email = forms.EmailField(required = True)
    username = forms.CharField(required = True, strip=False)

    #Nested namespace for configurations
    class Meta:
        #we specify what we want this model to interact with
        model = Account 
        #these are the feilds we want shown on our form and in what order
        fields = ['username','display_name', 'email','password1', 'password2']

    def clean_email(self):
        if self.is_valid:
            email= self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use' % account)

    def clean_username(self):
        if self.is_valid:
            username = self.cleaned_data['username']
            print(type(username))
            if not username.isalnum():
                raise forms.ValidationError('User "%s" is not valid' % username)
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('User "%s" is already in use' % username)

#model forms allow us to work with a specific database model (Tuple)
#this one will work with our User tuple
class UserUpdateForm(forms.ModelForm):


    #email = forms.EmailField(required = True)
    #username = forms.CharField(required = True, strip=False )
    #Nested namespace for configurations
    class Meta:
        #we specify what we want this model to interact with
        model = Account
        #these are the feilds we want shown on our form and in what order
        fields = ['username', 'email','display_name']

    def clean_email(self):
        if self.is_valid:
            email= self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use' % account)

    def clean_username(self):
        if self.is_valid:
            username = self.cleaned_data['username']
            print(type(username))
            if not username.isalnum():
                raise forms.ValidationError('User "%s" is not valid' % username)
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('User "%s" is already in use' % username)
            
#This works with the Profile Tuple and updates that
class ProfileUpdateForm(forms.ModelForm):
    class  Meta: 
        model = Profile
        fields = ['image']