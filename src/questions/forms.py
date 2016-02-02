from django import forms

class QuestionForm(forms.Form):
	title = forms.CharField(label='Title', max_length=100, 
		widget=forms.TextInput(attrs={'class' : 'form-control inputInfo'}))
	text = forms.CharField(label='Text', 
		widget=forms.Textarea(attrs={
			'class' : 'form-control inputInfo',
			'rows' : 10,
			}))
	tags = forms.CharField(label='Tags', max_length=200, 
		widget=forms.TextInput(attrs={'class' : 'form-control inputInfo'}))