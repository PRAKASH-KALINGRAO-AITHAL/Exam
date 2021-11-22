from django.db import models
from . import views
class Student(models.Model):
    RegNum=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    CGPA=models.FloatField()
   
    

    
