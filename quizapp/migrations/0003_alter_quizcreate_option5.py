# Generated by Django 4.1 on 2022-09-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_alter_quizcreate_options_quizcreate_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizcreate',
            name='option5',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
