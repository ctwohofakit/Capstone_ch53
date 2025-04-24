from django import forms
from .models import Interview

class InterviewSetupForm(forms.ModelForm):
    class Meta:
        model= Interview
        fields=['wanted_role','company_name','question_type','technology']
    
class AnswerForm(forms.Form):
    user_answer=forms.CharField(
        label="Your answer", 
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 50,
        })
    )