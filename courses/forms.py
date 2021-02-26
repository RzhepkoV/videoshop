from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'user', 'lesson']
        widgets = {'user': forms.HiddenInput(), 'lesson': forms.HiddenInput()}
