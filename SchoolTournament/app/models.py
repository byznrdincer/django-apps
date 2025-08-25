from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50),
    student_number=models.IntegerField(),
    grade=models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Match(models.Model):
    team_a=models.CharField(max_length=50),
    team_b=models.CharField(max_length=50),
    date=models.DateField(),
    score_a=models.IntegerField()
    score_b=models.IntegerField()
    
    def __str__(self):
        return self.date

class Team(models.Model):
    name=models.CharField(max_length=50),
    coach=models.CharField(max_length=50)
    members=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name