from django.db import models
from  django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff = True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser = True')

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):
        if not username:
            raise ValueError(_('You must provide a username'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user



class Student(AbstractBaseUser, PermissionsMixin):
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
    username = models.CharField(_('username'), max_length=65, unique=True)
    email = models.EmailField(max_length=65, unique=True)
    department = models.CharField(max_length=65, choices=DEPARTMENT_CHOICES, default='COMPUTER SCIENCE', blank=False, null=False)
    course1 = models.CharField(max_length=65, choices=COURSE_CHOICES, blank=True, null=True)
    course2 = models.CharField(max_length=65, choices=COURSE_CHOICES,  blank=True, null=True)
    course3 = models.CharField(max_length=65, choices=COURSE_CHOICES, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'department']
    
    class Meta:
        verbose_name = 'Students'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.username


