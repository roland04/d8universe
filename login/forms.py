from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20, label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username', 'required': True, 'autofocus': True,})
    )
    password = forms.CharField(
        max_length=20, label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password',})
    )
