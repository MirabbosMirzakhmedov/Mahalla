from django import forms
from .models import Post, Comment, User, PostNeighbors, NeighborComment
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'full_text', 'image']
        labels = {'title': 'Post sarlavhasi', 'full_text': '', 'image': 'Rasm'}

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post sarlavhasi'
            }),
            'full_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Toʻliq matnni joylash'
            })
        }

class PostNeighborsForm(forms.ModelForm):
    class Meta:
        model = PostNeighbors
        fields = ['title', 'full_text', 'image']
        labels = {'title': 'Post sarlavhasi', 'full_text': '', 'image': 'Rasm'}

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post sarlavhasi'
            }),
            'full_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Toʻliq matnni joylash'
            })
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

class NeighborCommentForm(forms.ModelForm):
    class Meta:
        model = NeighborComment
        fields = ['comment_text']

        widgets = {
            'comment_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fikr yozish'
            })
        }


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ism'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Familiya'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Foydalanuvchi nomi'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>150 yoki undan kam belgi. Faqat harflar, raqamlar va @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Parol'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Parolingiz kamida 8 ta belgidan iborat boʻlishi kerak.</li><li>Parolingiz to\'liq raqamdan iborat bo\'lishi mumkin emas.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Boshqattan tering'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Tekshirish uchun avvalgidek parolni kiriting.</small></span>'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_pic', 'bio']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ism'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Familiya'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form',
                'placeholder': "O'zingiz haqingizda"
            }),
            'profile_pic': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }