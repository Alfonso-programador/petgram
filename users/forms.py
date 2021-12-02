from django import forms
from .models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'

	def clean_email(self):
		email = self.cleaned_data['email']
		email_existe = User.objects.filter(email=email).exists()
		if email_existe:
			raise forms.ValidationError('email is already in use')
		return email

	def clean_username(self):
		username = self.cleaned_data['username']
		username_existe = User.objects.filter(username=username).exists()
		if username_existe:
			raise forms.ValidationError('Username is already in use')
		return username
