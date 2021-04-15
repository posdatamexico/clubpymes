from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	lastname = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'name', 'lastname', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__()

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	lastname = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	username = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'name', 'lastname', 'email', 'last_login', 'is_active')

class PasswordChangingForm(PasswordChangeForm):
	password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
	password1 = forms.CharField(max_length=100,  widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
	password2 = forms.CharField(max_length=100,  widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

	class Meta:
		model = User
		fields = ('old_password', 'new_password1', 'new_password2')


