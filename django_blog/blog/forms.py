from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment , Post
from taggit.forms import TagWidget   # ✅ Import TagWidget from taggit

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class post(forms.Form):
#     title = forms.CharField(max_length=200)
#     content = forms.CharField(widget=forms.Textarea)
#     author = forms.CharField(max_length=100)

#     class Meta:
#         model = User    
#         fields = ['title', 'content', 'author']


class Post(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Add tags separated by commas (e.g. Django, Python, Web)",
        widget=forms.TextInput(attrs={'placeholder': 'Enter tags separated by commas'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={'placeholder': 'Enter tags separated by commas'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            tags_str = self.cleaned_data.get('tags', '')
            tags_list = [t.strip() for t in tags_str.split(',') if t.strip()]
            instance.tags.clear()
            instance.tags.add(*tags_list)

        return instance

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



class TagWidget(forms.TextInput):
    """
    Custom widget for entering tags as a comma-separated list.
    """
    def __init__(self, attrs=None):
        default_attrs = {'placeholder': 'Enter tags separated by commas (e.g. Django, Python, Web)'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)
