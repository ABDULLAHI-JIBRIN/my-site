from django import forms
from .models import *

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title','category','image','content'
        ]



class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['content']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']