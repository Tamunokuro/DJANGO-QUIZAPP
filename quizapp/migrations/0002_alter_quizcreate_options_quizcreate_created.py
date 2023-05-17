# Generated by Django 4.1 on 2022-09-01 13:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizcreate',
            options={'ordering': ('created',), 'verbose_name': 'Questions', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AddField(
            model_name='quizcreate',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]