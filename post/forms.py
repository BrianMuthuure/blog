from django import forms

from post.models import Post, Comment


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'image', 'content']


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

