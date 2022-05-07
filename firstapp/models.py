
from operator import mod
from turtle import title
from django.db import models

# Create your models here.


# class Author(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)


# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     authors = models.ManyToManyField(to=Author)



class Employee(models.Model):
    name = models.CharField(max_length=200)
    salary = models.IntegerField()
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    DOj = models.DateTimeField(auto_now_add= True)
    active = models.BooleanField(default=True)




    


    def __str__(self):
        return self.name


class Meta:
    db_table = "emp"


    
