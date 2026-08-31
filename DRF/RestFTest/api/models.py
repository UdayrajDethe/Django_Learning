from django.db import models


# Create your models here.

#Creating comany model
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    type_of_company = models.CharField(max_length=50,choices=[('IT','IT'),
                                                              ('Finance','Finance'),
                                                              ('Manufacturing','Manufacturing')])
    about = models.TextField()
    date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name +' '+ self.location

#Emp Models
    
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    position = models.CharField(max_length=50, choices=[('Manager', 'Manager'),
                                                        ('Developer', 'Developer'),
                                                        ('Designer', 'Designer'),
                                                        ('QA', 'QA')])
    date_joined = models.DateTimeField(auto_now_add=True)