import re
from statistics import mode
from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    
    quiz_name = models.CharField(max_length=265, null=False, db_index=True)
    slug = models.SlugField(max_length=265, unique=True)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.quiz_name

    def course_get_absolute_url(self):
        return reverse('quizapp:questions', args=[self.slug])

class QuizCreate(models.Model):
    DEPARTMENT_CHOICES = (
        ("-----", "------"),
        ("COMPUTER SCIENCE", "COMPUTER SCIENCE"),
        ("MATHEMATICS & STATISTICS", "MATHEMATICS & STATISTICS"),
        ("COMPUTER INFO SYSTEM", "COMPUTER INFO SYSTEM")
    )
    COURSE_CHOICES = (
    ("-----", "------"),
    ("DATA STRUCTURES & ALGORITHM", "DATA STRUCTURES & ALGORITHM"),
    ("INTRODUCTION TO DATA SCIENCE", "INTRODUCTION TO DATA SCIENCE"),
    ("ARTIFICIAL INTELLIGENCE", "ARTIFICIAL INTELLIGENCE"),
    ("ANALYTICS", "ANALYTICS")
    )
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quizcreator_student')
    course_name = models.ForeignKey(Course, max_length=256, null=False, blank=False, on_delete=models.CASCADE, default="")
    creator_department = models.CharField(max_length=265, null=False, blank=False, choices=DEPARTMENT_CHOICES)
    created = models.DateField(auto_now_add=True)
    question = models.CharField(max_length=500, null=True)
    option1 = models.CharField(max_length=500, null=True)
    option2 = models.CharField(max_length=500, null=True)
    option3 = models.CharField(max_length=500, null=True)
    option4 = models.CharField(max_length=500, null=True)
    option5 = models.CharField(max_length=500, null=True, blank=True)
    answer = models.CharField(max_length=500, null=False, default='option1')

    class Meta:
        ordering = ('created',)
        verbose_name = 'Questions'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question


class QuizStudent(models.Model):
    DEPARTMENT_CHOICES = (
        ("-----", "------"),
        ("COMPUTER SCIENCE", "COMPUTER SCIENCE"),
        ("MATHEMATICS & STATISTICS", "MATHEMATICS & STATISTICS"),
        ("COMPUTER INFO SYSTEM", "COMPUTER INFO SYSTEM")
    )
    COURSE_CHOICES = (
    ("-----", "------"),
    ("DATA STRUCTURES & ALGORITHM", "DATA STRUCTURES & ALGORITHM"),
    ("INTRODUCTION TO DATA SCIENCE", "INTRODUCTION TO DATA SCIENCE"),
    ("ARTIFICIAL INTELLIGENCE", "ARTIFICIAL INTELLIGENCE"),
    ("ANALYTICS", "ANALYTICS")
    )
    OPTION_CHOICES = (
        ("option1", "OPTION1"),
        ("option2", "OPTION2"),
        ("option3", "OPTION3"),
        ("option4", "OPTION4")
    )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quiz_student') 
    quiz_course = models.ForeignKey(Course, max_length=256, null=False, blank=False, on_delete=models.CASCADE, default="")
    score = models.IntegerField(null=True, blank=True)
    time_taken = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.student




    