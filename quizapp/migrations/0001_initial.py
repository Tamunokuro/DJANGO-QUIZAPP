# Generated by Django 4.1 on 2022-09-01 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('-----', '------'), ('COMPUTER SCIENCE', 'COMPUTER SCIENCE'), ('MATHEMATICS & STATISTICS', 'MATHEMATICS & STATISTICS'), ('COMPUTER INFO SYSTEM', 'COMPUTER INFO SYSTEM')], max_length=256)),
                ('quiz_course', models.CharField(choices=[('-----', '------'), ('DATA STRUCTURES & ALGORITHM', 'DATA STRUCTURES & ALGORITHM'), ('INTRODUCTION TO DATA SCIENCE', 'INTRODUCTION TO DATA SCIENCE'), ('ARTIFICIAL INTELLIGENCE', 'ARTIFICIAL INTELLIGENCE'), ('ANALYTICS', 'ANALYTICS')], max_length=256)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(choices=[('-----', '------'), ('DATA STRUCTURES & ALGORITHM', 'DATA STRUCTURES & ALGORITHM'), ('INTRODUCTION TO DATA SCIENCE', 'INTRODUCTION TO DATA SCIENCE'), ('ARTIFICIAL INTELLIGENCE', 'ARTIFICIAL INTELLIGENCE'), ('ANALYTICS', 'ANALYTICS')], max_length=256)),
                ('creator_department', models.CharField(choices=[('-----', '------'), ('COMPUTER SCIENCE', 'COMPUTER SCIENCE'), ('MATHEMATICS & STATISTICS', 'MATHEMATICS & STATISTICS'), ('COMPUTER INFO SYSTEM', 'COMPUTER INFO SYSTEM')], max_length=265)),
                ('question', models.CharField(max_length=500, null=True)),
                ('option1', models.CharField(max_length=500, null=True)),
                ('option2', models.CharField(max_length=500, null=True)),
                ('option3', models.CharField(max_length=500, null=True)),
                ('option4', models.CharField(max_length=500, null=True)),
                ('option5', models.CharField(max_length=500, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizcreator_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
