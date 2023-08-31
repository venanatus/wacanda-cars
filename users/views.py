from django.contrib.auth import login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm, EditProfileForm, ResetPasswordForm


# def sign_up(request):
#     form = SignUpForm(data=request.POST)
#     is_success = False
#     is_error = False
#     if request.method == "POST" and form.is_valid():
#         print(SignUpForm)
#         form.save()
#         user = form.username
#         login(request, user)
#         # return redirect('users:sign_in')
#     return render(request, 'sign_up.html', {'form': form, 'is_success': is_success})
def sign_up(request):
    is_error = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # if len(form.password1) < 5:
        #     is_error = True
        if form.is_valid():
            user = form.save()
            print(form.password1)
            print('signed')
            login(request, user)

            return redirect('cars:home')
    form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form, 'is_error': is_error})


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
