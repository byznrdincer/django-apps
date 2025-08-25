from django import forms
from . models import Student
from . models import Match
from . models import Team

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','student_number','grade']
        
class TeamForm(forms.ModelForm):
    class Meta:
        model=Team
        fields=['name','coach','members']
        
class MatchForm(forms.ModelForm):
    class Meta:
        model=Match
        fields=['team_a','team_b','score_a','score_b','date']