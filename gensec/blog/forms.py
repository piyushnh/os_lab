from django import forms

from .models import Comment

class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
