from django import forms
from .models import Post

# forms.ModelForm - form related to ModelForm(db)
class PostForm(forms.ModelForm):

    # used to define what model will be used (Post, Get)
    # define the fields that will be in the form
    class Meta:
        model = Post
        fields = ('title', 'text',)