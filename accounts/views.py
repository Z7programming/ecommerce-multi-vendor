from django.shortcuts import render, redirect
from .form import sign_upForm, profileForm, userForm
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

#  ------------- sign_up -----------------


def sign_up(request):
    form = sign_upForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = sign_upForm()
    ctxt = {
        'title': 'sign_up',
        'form': form
    }
    return render(request, 'registration/sign_up.html', ctxt)

 #  ------------- profile -----------------


@login_required
def profile(request):
    userLogin = request.user
    prof = Profile.objects.get(user=userLogin)
    if request.method == 'POST':
        user_form = userForm(request.POST,  instance=userLogin)
        prof_form = profileForm(request.POST, request.FILES, instance=prof)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            print('#'*40)
    else:
        user_form = userForm(instance=userLogin)
        prof_form = profileForm(instance=prof)

    ctxt = {
        'title': userLogin.username,
        'prof': prof,
        'formuser': user_form,
        'formprofile': prof_form,
    }
    return render(request, 'profile.html', ctxt)

    # print('#'*40)
    # print('#'*40)
