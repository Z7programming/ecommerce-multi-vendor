from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.







@login_required
def vindor_dach(request):
  user = request.user.username 
  ctxt = {
    'title' : f'dachboard-{ user }'
  }
  return render(request,'vendor/vindor_dach.html',ctxt)