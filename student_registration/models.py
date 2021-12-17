from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    # student_code = models.CharField(max_length=3,default='STU')
    # mobile= models.CharField(max_length=15)
    department= models.ForeignKey(Department,on_delete=models.CASCADE)