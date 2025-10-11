from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class post(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=100)

    class Meta:
        model = User    
        fields = ['title', 'content', 'author']

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # We only want users to type their comment text
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment here...',
                'class': 'form-control',
            }),
        }
        labels = {
            'content': 'Add a comment',
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or content.strip() == "":
            raise forms.ValidationError("Comment cannot be empty.")
        return content
