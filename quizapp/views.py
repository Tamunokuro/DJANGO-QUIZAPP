import json
from json.decoder import JSONDecodeError
from urllib import request, response
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateQuestion
from .models import QuizCreate, QuizStudent, Course
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .quiz import Quiz
from users.models import Student
from django.http import JsonResponse
# Create your views here.
@login_required
def home(request):
    courses = Course.objects.all()
    return render(request, 'quizapp/index.html', {'courses':courses})

@login_required
def create_question(request):
    if request.method == 'POST':
        questionForm = CreateQuestion(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=True)
            question.save()

            response = redirect('/')
            return response

    else:
        questionForm = CreateQuestion()
    return render(request, 'quizapp/create-question.html', {'form':questionForm})

def questions(request, quiz_name=None):
    if request.method == "GET":
        course = get_object_or_404(Course, slug=quiz_name)
        allquestions = QuizCreate.objects.filter(course_name=course)
        p = Paginator(allquestions, 1)
        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)


        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)

        return render(request, 'quizapp/questions.html', {'questions':allquestions,'page_obj': page_obj, 'course': course})


    elif request.method == "POST":
        #selected answer should be gotten from the front end using request.POST.get('name')
        #compare selected answer with correct answer
        #return a message to tell if answer is correct or wrong
        #if correct return success message
        #if wrong return error message
        selected_answer = request.POST.get('option')
        correct_answer = request.POST.get('answer')
        if selected_answer == correct_answer:
            messages.success(request, "🎉 Correct Answer")

        else:
            messages.warning(request, "⛔ Wrong answer")

        next_page_number = int(request.GET.get('page', 1))  # Assuming you're using query parameter 'page' to determine the current page
        next_page_url = reverse('quizapp:questions', kwargs={'quiz_name': quiz_name}) + f'?page={next_page_number}'
        return HttpResponseRedirect(next_page_url)
