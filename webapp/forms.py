from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'full_text', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post sarlavhasi'
            }),
            'full_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Toʻliq matnni joylash'
            }),
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

        widgets = {
            'comment_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fikr yozish'
            })
        }

