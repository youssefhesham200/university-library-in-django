from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser) :
    is_owner = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    identification = models.IntegerField(verbose_name="identification Number", default=0)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class FormBook(models.Model):
    statusBook = [
        ('borrowed', 'borrowed'),
        ('available', 'available'),
    ]
    bookName = models.CharField(max_length=50, verbose_name="Book's name", default=None)
    author = models.CharField(max_length=50, verbose_name="author's name", default=None)
    isbn = models.IntegerField(verbose_name="ISBN", default=0)
    pop = models.IntegerField(verbose_name="publication year", default=0)
    status = models.CharField(max_length=50, choices=statusBook, null=True, blank=True, default='available')
    returning = models.IntegerField(default=0, verbose_name="borrowing period")