from django import forms
class LoginForm(forms.Form):
	username = forms.CharField( max_length=30)
	password = forms.CharField( widget=forms.PasswordInput)
class RegForm(forms.Form):
	username = forms.CharField( max_length=30)
	password = forms.CharField( widget=forms.PasswordInput)
	email = forms.EmailField()
	isA = forms.CharField(max_length = 3)
	isB = forms.CharField(max_length = 3)
	isC = forms.CharField(max_length = 3)
	isD = forms.CharField(max_length = 3)
	isE = forms.CharField(max_length = 3)
	isF = forms.CharField(max_length = 3)
	isG = forms.CharField(max_length = 3)
	isH = forms.CharField(max_length = 3)
	isI = forms.CharField(max_length = 3)
	city = forms.CharField( max_length=30)
	neighbourhood = forms.CharField( max_length=30)
class forgetpassword(forms.Form):
	email = forms.EmailField()