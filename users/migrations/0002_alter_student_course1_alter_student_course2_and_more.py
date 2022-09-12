# Generated by Django 4.1 on 2022-08-31 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course1',
            field=models.CharField(blank=True, choices=[('-----', '------'), ('DATA STRUCTURES & ALGORITHM', 'DATA STRUCTURES & ALGORITHM'), ('INTRODUCTION TO DATA SCIENCE', 'INTRODUCTION TO DATA SCIENCE'), ('ARTIFICIAL INTELLIGENCE', 'ARTIFICIAL INTELLIGENCE'), ('ANALYTICS', 'ANALYTICS')], max_length=65, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='course2',
            field=models.CharField(blank=True, choices=[('-----', '------'), ('DATA STRUCTURES & ALGORITHM', 'DATA STRUCTURES & ALGORITHM'), ('INTRODUCTION TO DATA SCIENCE', 'INTRODUCTION TO DATA SCIENCE'), ('ARTIFICIAL INTELLIGENCE', 'ARTIFICIAL INTELLIGENCE'), ('ANALYTICS', 'ANALYTICS')], max_length=65, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='course3',
            field=models.CharField(blank=True, choices=[('-----', '------'), ('DATA STRUCTURES & ALGORITHM', 'DATA STRUCTURES & ALGORITHM'), ('INTRODUCTION TO DATA SCIENCE', 'INTRODUCTION TO DATA SCIENCE'), ('ARTIFICIAL INTELLIGENCE', 'ARTIFICIAL INTELLIGENCE'), ('ANALYTICS', 'ANALYTICS')], max_length=65, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('-----', '------'), ('COMPUTER SCIENCE', 'COMPUTER SCIENCE'), ('MATHEMATICS & STATISTICS', 'MATHEMATICS & STATISTICS'), ('COMPUTER INFO SYSTEM', 'COMPUTER INFO SYSTEM')], default='COMPUTER SCIENCE', max_length=65),
        ),
    ]
