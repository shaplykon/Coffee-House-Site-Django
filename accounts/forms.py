from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(forms.Form):
    username = forms.EmailField(label='Enter Email', min_length=4, max_length=150)
    email = forms.CharField(label='Enter Username')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class DeleteAccountForm(forms.Form):
    email = forms.CharField(label='Enter email')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            return email
        raise forms.ValidationError("Email does not exist")


class UserInfoForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150, widget=forms.TextInput)
    email = forms.EmailField(label='Enter email')
    first_name = forms.CharField(label='Enter First Name', min_length=4, max_length=150, widget=forms.TextInput)
    last_name = forms.CharField(label='Enter Last Name', min_length=4, max_length=150, widget=forms.TextInput)

    def get_username(self, request):
        username = self.cleaned_data['username'].lower()
        r = list(User.objects.filter(username=username))
        if len(r) == 1 and r[0].username != request.user.username:
            raise forms.ValidationError("Username already exists")
        return username

    def get_email(self, request):
        email = self.cleaned_data['email'].lower()
        r = list(User.objects.filter(email=email))
        if len(r) == 1 and r[0].email != request.user.email:
            raise forms.ValidationError("Email already exists")
        return email

    def get_first_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        return first_name

    def get_last_name(self):
        last_name = self.cleaned_data['last_name'].lower()
        return last_name

    def set_placeholders(self):
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last name'})


class UpdatePictureForm(forms.Form):
    picture = forms.ImageField(label='Select a picture')
