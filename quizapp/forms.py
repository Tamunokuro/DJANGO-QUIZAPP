from dataclasses import fields
from .models import *
from django import forms

class CreateQuestion(forms.ModelForm):
    class Meta: 
        model = QuizCreate
        fields = "__all__"

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['creator'].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': 'Username'})
            self.fields['creator_department'].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': 'Author', 'name': 'creator_department', 'id': 'creator_department'})
            self.fields['course_name'].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': 'Select Course', 'name': 'course_name', 'id': 'id_course_name'})
            self.fields['question'].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': 'Create Question', 'name': 'question', 'id': 'question'})
            self.fields['option1'].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': 'A', 'name': 'option1', 'id': 'id_option1'})
            self.fields['option2'].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': 'B', 'name': 'option2', 'id': 'id_option2'})
            self.fields['option3'].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': 'C', 'name': 'option3', 'id': 'id_option3'})
            self.fields['option4'].widget.attrs.update(
                {'class': 'form-control', 'placeholder': 'D', 'name': 'option4', 'id':'id_option_4'})

class TakeQuiz(forms.ModelForm):
    class Meta:
        model = QuizStudent
        fields = "__all__"

    def __int__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.fields['question'].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': 'Student', 'id':'student', 'readonly':'readonly'})
        self.fields['option1'].widget.attrs.update(
                {'class': 'form-check-input mb-3','type':'radio', 'name': 'option1', 'id': 'id_option1'})


  
