from django.urls import path
from . import views

app_name = 'quizapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('create-question/', views.create_question, name='create-question'),
    path('questions/<slug:quiz_name>', views.questions, name='questions'),
]