from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','blog_text']

        # for custom forms for adding a blog!!
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'blog_text' : forms.Textarea(attrs={'class':'form-control'})
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    # apply Bootstrap classes to password fields
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class':'form-control'})
