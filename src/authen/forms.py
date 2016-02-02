from django import forms

class UserForm(forms.Form):
	login = forms.CharField(label='Login', max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control inputInfo'},
		))
	nick = forms.CharField(label='Nick', max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control inputInfo'}))
	password = forms.CharField(label='Password', max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control inputInfo'}))