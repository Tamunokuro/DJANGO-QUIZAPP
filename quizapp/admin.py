from django.contrib import admin
from .models import QuizCreate, QuizStudent, Course

# Register your models here.
class QuizCreateAdmin(admin.ModelAdmin):
    list_display = ['question', 'course_name','answer', 'creator', 'creator_department']
    
class CourseAdmin(admin.ModelAdmin):
    list_display= ['quiz_name']
    prepopulated_fields = {'slug': ('quiz_name',)}

class QuizStudentAdmin(admin.ModelAdmin):
    list_display = ['student','department', 'quiz_course', 'score', 'time_taken']


admin.site.site_header = 'QUIZ APP ADMIN'
admin.site.register(QuizCreate, QuizCreateAdmin)
admin.site.register(QuizStudent, QuizStudentAdmin)
admin.site.register(Course, CourseAdmin)