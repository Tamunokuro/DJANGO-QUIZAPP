
from urllib import request, response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateQuestion, TakeQuiz
from .models import QuizCreate, QuizStudent, Course
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .quiz import Quiz
from users.models import Student
from django.http import JsonResponse
# Create your views here.
@login_required
def home(request):
    courses = Course.objects.all()
    questionForm = TakeQuiz()
    return render(request, 'quizapp/index.html', {'form':questionForm, 'courses':courses})

@login_required
def create_question(request):
    if request.method == 'POST':
        questionForm = CreateQuestion(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=True)
            question.save()

            response = redirect('/questions/')
            return response

    else:
        questionForm = CreateQuestion()
    return render(request, 'quizapp/create-question.html', {'form':questionForm})

def questions(request, quiz_name=None):
    quiz = Quiz(request)
    if request.method == "POST":
        quizform = TakeQuiz(request.POST)
        if quizform.is_valid():
            quiz = quizform.save()
            quiz.save()
            response = redirect('/questions/')
            return response
    else:
        course = get_object_or_404(Course, slug=quiz_name)
        allquestions = QuizCreate.objects.filter(course_name=course)

        # for question in allquestions:
        #     print({question.question: question.answer} )

        p = Paginator(allquestions, 1)
        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)


        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)
        
    return render(request, 'quizapp/questions.html', {'questions':allquestions,'page_obj': page_obj, 'course': course})

def quiz_answer(request):

    quiz = Quiz(request)
    if request.POST.get('action') == "POST":
        student_id = request.POST.get('student')
        question_value = request.POST.get('questionval')
        question_option = request.POST.get('questionans')
        question_answer = request.POST.get('answer')
        # student = get_object_or_404(Student, id=username)
        quiz.answer(q=question_value, option=question_option)
        score = quiz.score( option=question_option, correct=question_answer)
        response = JsonResponse({'question':question_value, 'answer':question_option,
         'correct':question_answer, 'student':student_id})
        return response

def answer_update(request):
    quiz = Quiz(request)
    if request.POST.get('action') == 'POST':
        student_id = request.POST.get('student')
        question_value = request.POST.get('questionval')
        question_option = request.POST.get('questionans')
        question_answer = request.POST.get('answer')
        quiz.update_answer(student=student_id, q=question_value, option=question_option)
        response = JsonResponse({'question':question_value, 'answer':question_option,
         'correct':question_answer, 'student':student_id})
        return response