from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserOurRegistration, ProfileImage, UserUpdateForm, GenderPlusAcceptForm


def register(request):
    if request.method == "POST":
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был создан, введите имя пользователя и пароль для авторизации')
            return redirect('user')
    else:
        form = UserOurRegistration()
    return render(request, 'users/registraion.html', {'form': form, 'title': 'Регистрация пользователя'})


@login_required
def profile(request):
    if request.method == "POST":
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)
        genderAndAccept = GenderPlusAcceptForm(request.POST, instance=request.user.profile)

        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            genderAndAccept.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)
        genderAndAccept = GenderPlusAcceptForm(instance=request.user.profile)

    data = {
        'img_profile': img_profile,
        'update_user': update_user,
        'genderAndAccept': genderAndAccept
    }

    return render(request, 'users/profile.html', data)
