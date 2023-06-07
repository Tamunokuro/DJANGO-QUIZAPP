from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import CreateQuestion
from .models import QuizCreate, QuizStudent, Course
from .quiz import Quiz
from users.models import Student
from urllib import request, response

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
        questions_count = allquestions.count()
        p = Paginator(allquestions, questions_count | 1)
        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)


        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)

        return render(request, 'quizapp/questions.html', {'questions':allquestions,'page_obj': page_obj, 'course': course})


    if request.method == "POST":
        #selected answer should be gotten from the front end using request.POST.get('name')
        #compare selected answer with correct answer
        #return a message to tell if answer is correct or wrong
        #if correct return success message
        #if wrong return error message
        questions = QuizCreate.objects.filter(course_name__slug=quiz_name)
        score = 0
        for question in questions:
            answer_selected = f'option{question.id}'
            answer_correct = question.answer
            selected_answer = request.POST.get(answer_selected)
            course = request.POST.get("course_title")
            if selected_answer == answer_correct:
                score += 1
                messages.success(request, "🎉 Correct Answer")
            else:
                messages.warning(request, "⛔ Wrong answer")

        percentage_score = (score / questions.count()) * 100
        formatted_score = '{:.0f}'.format(percentage_score)
        final_score = int(formatted_score)
        
        user=request.user
        course_title = request.POST.get("course_title")
        course = Course.objects.get(quiz_name=course_title)
        result = QuizStudent(student=user, quiz_course=course, score=final_score)
        result.save()
        return HttpResponseRedirect(reverse('quizapp:questions', kwargs={'quiz_name': course_title.lower()}))
        