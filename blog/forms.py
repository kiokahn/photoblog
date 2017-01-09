from django.forms import ModelForm
from blog.models import *

class Form(ModelForm):
    class Meta:
        model = Post
        fields=['title', 'contents']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        #fields='__all__'
        fields=('author', 'message')
