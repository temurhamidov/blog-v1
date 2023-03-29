from django import forms
from .models import Blog, Comment


class BlogAddForms(forms.ModelForm):

    tags = forms.CharField(max_length=200)

    class Meta:
        model = Blog
        fields = [
            'title',
            'image',
            'text',
            'category',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BlogUpdateForms(forms.ModelForm):

    class Meta:
        model = Blog
        fields = [
            'title',
            'image',
            'text',
            'category',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
