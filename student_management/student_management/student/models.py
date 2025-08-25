from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    student_number=models.IntegerField()
    grade=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return self.name
    