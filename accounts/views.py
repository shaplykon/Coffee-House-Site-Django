from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, DeleteAccountForm, UserInfoForm, UpdatePictureForm

User = get_user_model()


def register_form(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            form = CustomUserCreationForm
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = CustomUserCreationForm

    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm

    return render(request, 'registration/login.html', {'form': form})


def account_view(request):
    if request.method == 'POST':
        delete_form = DeleteAccountForm(data=request.POST)
        if delete_form.is_valid():
            user = User.objects.filter(email=delete_form.clean_email())
            if user[0].email == request.user.email:
                user.delete()
                return redirect('index')
        return render(request, 'registration/account.html', {'delete_form': delete_form, 'user': request.user})
    else:
        delete_form = DeleteAccountForm
        form = UserInfoForm(initial={'username': request.user.username, 'email': request.user.email,
                                     'first_name': request.user.first_name,
                                     'last_name': request.user.last_name})

        form.set_placeholders()
        user = request.user
        picture_form = UpdatePictureForm
        return render(request, 'registration/account.html',
                      {'delete_form': delete_form, 'user': user, 'form': form, 'picture_form': picture_form})


def change_avatar(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        update_picture_form = UpdatePictureForm(data=request.POST, files=request.FILES)
        if update_picture_form.is_valid():
            picture = request.FILES['picture']
            print(picture.size)
            print(picture.name)
            user.picture = picture
            print(user.picture)
            user.save()

    return redirect('account', 'registration/account.html',
                    {'user': request.user})


def save_changes(request):
    if request.method == 'POST':
        user_info_form = UserInfoForm(data=request.POST)

        if user_info_form.is_valid():
            username = user_info_form.get_username(request)
            email = user_info_form.get_email(request)
            first_name = user_info_form.get_first_name()
            last_name = user_info_form.get_last_name()
            user = User.objects.get(id=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
    return redirect('account', 'registration/account.html',
                    {'user': request.user})
