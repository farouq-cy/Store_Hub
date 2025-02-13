from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']



class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, required=True)
    PhoneNumber = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ['username', 'PhoneNumber', 'email', 'role', 'password1', 'password2']

    def clean_PhoneNumber(self):
        phone_number = self.cleaned_data.get('PhoneNumber')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Phone number should contain only digits.")
        return phone_number
    



class CustomLoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("اسم المستخدم أو كلمة المرور غير صحيحة.")
            if not isinstance(user, User):  # التأكد إنه من الموديل المخصص
                raise forms.ValidationError("هذا الحساب غير مسموح له بتسجيل الدخول.")

        return cleaned_data