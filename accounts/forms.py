from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, UserProfile


class AccountSignupForm(UserCreationForm):
    first_name=forms.CharField(
    required=True,
    widget=forms.TextInput(attrs={
        "class":"contact-input",
        "placeholder":"first name",
    })
    )
    last_name=forms.CharField(
    required=True,
    widget=forms.TextInput(attrs={
        "class":"contact-input",
        "placeholder":"last name",
    })
    )
    email=forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class":"contact-input",
            "placeholder":"you@example.com",
        })
    )
    password1=forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"contact-input",
            "placeholder":"Password",
        })
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"contact-input",
            "placeholder":"Password",
        })
    )

    class Meta:
        model=Account
        fields=("first_name","last_name","email","password1","password2")



class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=[
            "profile_picture",
            "address_line_1",
            "address_line_2",
            "city",
            "state",
            "country",
            "zip_code"
        ]
        widgets={
            "profile_picture":forms.ClearableFileInput(attrs={
                "class":"user-profile-pic",
            })
        }

class ProfilePic(forms.ModelForm):
    class Meta:
        mdoel=UserProfile
        