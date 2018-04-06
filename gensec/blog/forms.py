from django import forms

from .models import Comment

class CommentReplyForm(forms.ModelForm):
    class meta:
        model = Comment
        fields = ('text') 
