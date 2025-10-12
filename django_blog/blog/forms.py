from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment , Post , Tag
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


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Add tags separated by commas (e.g. Django, Python, Web)"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            tags_str = self.cleaned_data.get('tags', '')
            tags_list = [t.strip() for t in tags_str.split(',') if t.strip()]
            instance.tags.clear()
            for tag_name in tags_list:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)
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
