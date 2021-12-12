from django.utils.translation import gettext_lazy as _
from django import forms

from .errors import ErrorMessages
from .models import CustomUser
from .validators import is_password_valid


class RegistrationForm(forms.ModelForm):
    
    password = forms.CharField(min_length=6, max_length=30, widget=forms.PasswordInput())
    confirm_password = forms.CharField(min_length=6, max_length=30, widget=forms.PasswordInput())
    patronymic = forms.CharField(max_length=30, required=False, widget=forms.TextInput())
    
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password',
            'confirm_password',
            'first_name',
            'last_name',
            'patronymic',
        ]
        widgets = {
            'email': forms.EmailInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
        }
        
    def clean(self):
        """Redefined method clean from ModelForm to add password confimation

        Raises:
            forms.ValidationError: 
                - raise if password and confirm password don't match
                - raise of password doesn't contain at least 1 character and at least 1 number
        """
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if not is_password_valid(password):
            raise forms.ValidationError(ErrorMessages.PASSWORD_VALIDATION_ERROR)
        if password != confirm_password:
            raise forms.ValidationError(ErrorMessages.PASSWORD_NOT_MATCH_ERROR)
    
    def save(self, commit=True):
        """Redefined method save from ModelForm

        Args:
            commit (bool, optional): 
            set to True in case to commit changes, set to False to get user object without commiting. Defaults to True.

        Returns:
            CustomUser: user object
        """
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
        return user


class LoginForm(forms.ModelForm):
    
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    
    class Meta:
        model = CustomUser
        fields = ['email']
