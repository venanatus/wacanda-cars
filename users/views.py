from django.contrib.auth import login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm, EditProfileForm, ResetPasswordForm


def sign_up(request):
    form = SignUpForm(request.POST or None)
    is_success = False
    is_not_short = True
    if len(form.password1) < 5:
        is_not_short = False

    if request.method == "POST" and form.is_valid() and is_not_short == True:
        form.save()
        is_success = True
        # return redirect('users:sign_in')
    return render(request, 'sign_up.html', {'form': form, 'is_success': is_success, 'is_not_short': is_not_short})


def sign_in(request):
    form = SignInForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('cars:home')
    return render(request, 'sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('users:sign_in')
