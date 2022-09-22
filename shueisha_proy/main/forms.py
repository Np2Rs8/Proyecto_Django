"""
	    Importacion de librerias necesarias
"""
from django import forms

from .models import Blog
from .models import Review

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User

"""
	Formulario para crea el usuario.
"""
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']


"""
	Formulario para crear los blogs.
"""
class BlogForm(forms.ModelForm):

	
	author = forms.CharField(max_length=50, required=True,
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'id': 'author',
			'name': 'author',
			'placeholder': '*Autor...',
			}))
	

	name = forms.CharField(max_length=50, required=True,
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': '*Nombre...',
			}))
	description = forms.CharField(max_length=1000, required=True,
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': '*Descripción...',
			'rows':'4'
			}))
	body = forms.CharField(max_length=10000, required=True, 
		widget=forms.Textarea(attrs={
			'class': 'form-control',
			'placeholder': '*Blog...',
			'rows': 8,
			}))
	image = forms.ImageField()

	class Meta:
		
		model = Blog
		fields = ('author', 'name', 'description', 'body', 'image')


"""
	Formulario para crear las reviews
"""
class ReviewForm(forms.ModelForm):

	author = forms.CharField(max_length=50, required=True,
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'id': 'author',
			'name': 'author',
			'placeholder': '*Autor...',
			}))
	name = forms.CharField(max_length=50, required=True,
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': '*Nombre...',
			}))
	description = forms.CharField(max_length=1000, required=True,
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': '*Descripción...',
			'rows':'4'
			}))
	body = forms.CharField(max_length=10000, required=True, 
		widget=forms.Textarea(attrs={
			'class': 'form-control',
			'placeholder': '*Blog...',
			'rows': 8,
			}))
	image = forms.ImageField()

	class Meta:
		model = Review
		fields = ('author', 'name', 'description', 'body', 'image')
