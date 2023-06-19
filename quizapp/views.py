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
    return render(request, "quizapp/index.html", {"courses": courses})


@login_required
def create_question(request):
    if request.method == "POST":
        questionForm = CreateQuestion(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=True)
            question.save()

            response = redirect("/")
            return response

    else:
        questionForm = CreateQuestion()
    return render(request, "quizapp/create-question.html", {"form": questionForm})


def questions(request, quiz_name=None):
    if request.method == "GET":
        course = get_object_or_404(Course, slug=quiz_name)
        allquestions = QuizCreate.objects.filter(course_name=course)
        questions_count = allquestions.count()
        p = Paginator(allquestions, questions_count + 1)  # Use '+' instead of '|'
        page_number = request.GET.get("page")
        page_obj = p.get_page(page_number)

        context = {
            "questions": allquestions,
            "page_obj": page_obj,
            "course": course,
        }

        return render(request, "quizapp/questions.html", context)

    elif request.method == "POST":
        course_title = request.POST.get('course_title')
        score = 0
        for key, value in request.POST.items():
            if key.startswith('option'):
                question_id = int(key.split('option')[1])
                user_answer = value
                correct_answer = request.POST.get(f'answer_{question_id}')
            
                if user_answer == correct_answer:
                    score += 1
                    messages.success(request, "🎉 Correct Answer")
                else:
                    messages.warning(request, "⛔ Wrong answer")

        percentage_score = (score * 10)
        formatted_score = "{:.0f}".format(percentage_score)
        final_score = int(formatted_score)

        user = request.user
        course_title = request.POST.get("course_title")
        course = Course.objects.get(quiz_name=course_title)
        result = QuizStudent(student=user, quiz_course=course, score=final_score)
        result.save()
        return redirect('quizapp:questions', quiz_name=course.slug)