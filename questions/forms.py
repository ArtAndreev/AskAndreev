from django import forms


class LoginForm(forms.ModelForm):
    login = forms.EmailField(max_length=100)
    password = forms.PasswordInput()

    def clean_login(self):
        login = self.cleaned_data['login']
        if login is None:
            raise forms.ValidationError('Login is empty')

        class Meta:
            pass

