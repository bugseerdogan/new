from django.contrib.auth.models import User
from django import forms

from .models import Planning
class PlanForm(forms.ModelForm):

    class Meta:
        model = Planning
        fields = fields=['title','author','publication','quality','medium','planned_date','bl','applied_date','status','notes','is_AL','is_BL']
class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=['username','email','password']