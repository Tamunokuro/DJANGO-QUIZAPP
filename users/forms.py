from pyexpat import model
from random import choices
from django import forms
from  django.contrib.auth.models import User
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm)
from .models import Student

DEPARTMENT_CHOICES = [
     ("-----", "------"),
     ("COMPUTER SCIENCE", "COMPUTER SCIENCE"),
     ("MATHEMATICS & STATISTICS", "MATHEMATICS & STATISTICS"),
     ("COMPUTER INFO SYSTEM", "COMPUTER INFO SYSTEM"),

]

COURSE_CHOICES = [
    ("-----", "------"),
    ("DATA STRUCTURES & ALGORITHM", "DATA STRUCTURES & ALGORITHM"),
    ("INTRODUCTION TO DATA SCIENCE", "INTRODUCTION TO DATA SCIENCE"),
    ("ARTIFICIAL INTELLIGENCE", "ARTIFICIAL INTELLIGENCE"),
    ("ANALYTICS", "ANALYTICS"),

]

class AccountRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label='Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(label='Email', help_text='Required', error_messages={
        'required': 'Sorry!, you need an email address'})
    department = forms.ChoiceField(label="Select Department", choices= DEPARTMENT_CHOICES)
    course1 = forms.ChoiceField(label='Select Course', choices= COURSE_CHOICES)
    course2 = forms.ChoiceField(label='Select Course', choices= COURSE_CHOICES)
    course3 = forms.ChoiceField(label='Select Course', choices= COURSE_CHOICES)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['username', 'email','department','course1', 'course2', 'course3', 'password', 'password2']
        

    def clean_username(self):
        username = self.cleaned_data['username']
        r = Student.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exist")
        return username

    def check_password2(self):
        cp = self.cleaned_data
        if cp['password'] != cp['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cp['password2']

    def cleaned_email(self):
        email = self.cleaned_data['email']
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'An account has been registered with this email already'
            )
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username', 'name': 'username', 'id': 'id_username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['department'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Department', 'name': 'department', 'id': 'id_department'})
        self.fields['course1'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Select Course', 'name': 'course1', 'id': 'id_course1'})
        self.fields['course2'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Select Course', 'name': 'course2', 'id': 'id_course2'})
        self.fields['course3'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Select Course', 'name': 'course3', 'id': 'id_course3'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})

class AccountLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-user'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Password',
        'id': 'login-pwd'
    }))