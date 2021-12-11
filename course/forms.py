from django import forms
from django.utils.translation import gettext_lazy as _

from authentication.validators import is_password_valid
from .models import Course, UserCourse


class CourseCreateForm(forms.ModelForm):
    
    name = forms.CharField(max_length=128, widget=forms.TextInput())
    password = forms.CharField(max_length=20, min_length=6, widget=forms.PasswordInput())
    confrim_password = forms.CharField(max_length=20, min_length=6, widget=forms.PasswordInput())
    group_name = forms.CharField(max_length=60, required=False, widget=forms.TextInput())
    join_code = forms.CharField(max_length=20, min_length=5, widget=forms.TextInput())
    
    class Meta:
        model = Course
        fields = [
            'name',
            'group_name',
            'join_code',
        ]
        
    def clean(self):
        """Redefined clean method to validate password and cofirm_password

        Raises:
            forms.ValidationError: 
                - raise if password and confirm password don't match
                - raise of password doesn't contain at least 1 character and at least 1 number
        """
        cleaned_data = super(CourseCreateForm, self).clean()
        password = cleaned_data.get('password')
        confrim_password = cleaned_data.get('confrim_password')

        if not is_password_valid(password):
            raise forms.ValidationError(_('Passwrod should contains at least 1 character, at least 1 number'))
        if password != confrim_password:
            raise forms.ValidationError(_('Password and confirm password don\'t match'))
        
    def save(self, commit=True):
        """Redefined save method to set hashed course password

        Args:
            commit (bool, optional): Saves the model if commit=True. Defaults to True.

        Returns:
            Course: The new created course
        """
        course = super(CourseCreateForm, self).save(commit=False)
        course.set_password(self.cleaned_data['password'])
        
        if commit:
            course.save()
        return course


class CourseJoinForm(forms.ModelForm):
    
    password = forms.CharField(max_length=20, min_length=6, widget=forms.PasswordInput())
    
    class Meta:
        model = Course
        fields = [
            'join_code',
            'password'
        ]
