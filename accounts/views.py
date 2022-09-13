from django.shortcuts import render,redirect
from .form import sign_upForm
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

 #  ------------- sign_up -----------------
def sign_up(request):
  form =  sign_upForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      return redirect('login')
  else :
    form = sign_upForm()
  ctxt = { 
    'title' :'sign_up', 
    'form':form
  }
  return render(request, 'registration/sign_up.html',ctxt)

 #  ------------- profile -----------------
@login_required
def profile(request):
  userLogin  = request.user
  
  prof =Profile.objects.filter(user = userLogin)
 
  ctxt = { 
    'title' :userLogin.username,
    'prof' : prof,
  }
  return render(request,'profile.html',ctxt)