
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateQuestion, TakeQuiz
from .models import QuizCreate, QuizStudent, Course
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

        for question in allquestions:
            print({question.question: question.answer} )

        p = Paginator(allquestions, 4)
        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)

        # try:
        #     mystories = p.page(page_number)
        # except PageNotAnInteger:
        #     mystories = p.page(1)
        # except EmptyPage:
        #     mystories = p.page(p.num_pages)


        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)
    return render(request, 'quizapp/questions.html', {'questions':allquestions,'page_obj': page_obj, 'course': course})