from django import forms
from .models import *
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']



class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES, required=True)
    PhoneNumber = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'PhoneNumber', 'role']

    def clean_PhoneNumber(self):
        phone_number = self.cleaned_data.get('PhoneNumber')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("رقم الهاتف يجب أن يحتوي على أرقام فقط.")
        return phone_number

    def save(self, commit=True):
        user = super().save(commit=False)  # حفظ بيانات `User` بدون الحفظ النهائي
        if commit:
            user.save()  # حفظ المستخدم
            UserProfile.objects.create(  # إنشاء ملف `UserProfile`
                user=user,
                role=self.cleaned_data['role'],
                PhoneNumber=self.cleaned_data['PhoneNumber']
            )
        return user
    



class CustomLoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ' '})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("اسم المستخدم أو كلمة المرور غير صحيحة.")
            if not user.is_active:
                raise forms.ValidationError("هذا الحساب غير مفعل.")

        return cleaned_data