from django import forms
from .models import Book, CustomUser

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def clean_publication_year(self):
        year = self.cleaned_data.get("publication_year")
        if year and (year < 0 or year > 9999):
            raise forms.ValidationError("Invalid year.")
        return year


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'date_of_birth', 'profile_photo', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
