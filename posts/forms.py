from django import forms
from posts.models import Author


class PostForm(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField(required=False)
    author = forms.ChoiceField(
        choices=((a.id, a.nick) for a in Author.objects.all())
        )
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        author = cleaned_data.get('author')
       

class AuthorForm(forms.Form):
    nick = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    

    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        email = cleaned_data.get('email')
