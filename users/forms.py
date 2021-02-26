from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['img'].label = "Изображение профиля"

    class Meta:
        model = Profile
        fields = ['img']


class GenderPlusAcceptForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Выберете пол*',
        required=False,
        choices=Profile.gen,
        widget=forms.Select(attrs={'class': 'custom-select'})

    )
    accept = forms.BooleanField(
        label='Соглашение на отправку уведомлений на почту',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'})
    )

    class Meta:
        model = Profile
        fields = ['gender', 'accept']
