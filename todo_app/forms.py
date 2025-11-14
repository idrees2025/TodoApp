from django import forms
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Userform(UserCreationForm):
    email=forms.EmailField(max_length=222)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','Dsc','photo']
        widgets={
            'title':forms.TextInput(attrs={
                'placeholder' : 'Enter Title Here...',
                'style' :'width:10.3cm;'
            }),
            'Dsc':forms.Textarea(attrs={
                'placeholder':'Enter Description Here...'
            })
        }