from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta(UserCreationForm):
        model = User
        fields = (
            'email',
            'password1',
            'password2',
            # 'nickname',
            # 'phone_number',
            # 'profile_image',
            # 'preferences',
        )


class SigninForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        self.user = authenticate(
            email=email,
            password=password,
        )
        if not self.user:
            raise forms.ValidationError('Login Failed')
        else:
            setattr(self, 'signin', self._signin)

    def _signin(self, request):
        if self.user:
            login(request, self.user)
