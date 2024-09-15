from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagWidget  # Import TagWidget from django-taggit

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        widget=TagWidget(),  # Use TagWidget for handling tags
        required=False,
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']