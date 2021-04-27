from django import forms
from .models import Document
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DocumentForm(forms.Form):
    def is_valid(*args, **kwargs):
        return True

    file = forms.FileField(help_text='Valid .mp3 file')





# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user