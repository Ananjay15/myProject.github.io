from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from .forms  import AuhenticatePerson
from django.http import *
from datetime import datetime
from datetime import date
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from accounts.models import Registry
from django.forms.models import inlineformset_factory
from accounts.models import *
from django.contrib import messages



@api_view(['GET','POST'])
def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuhenticatePerson(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password'] 
                user = User.objects.filter(username=uname)
                for name in user:
                    email = name.email
                    join_date = name.date_joined
                    status = name.is_active

                print(join_date.date())
                valid = int((date.today() - join_date.date()).days)
                reg = Registry.objects.get(email=uname)
                print(valid)
                if valid == 366:
                    reg.is_active = False
                    reg.pending = True
                    reg.save()
                if reg.pending == True:
                    msg = 'Your Validity is expire.'
                    return render(request,'login_user.html',{'form':fm,'msg':msg})            
                else:
                    user = authenticate(username=uname,password=upass)
                    if user is not None:
                        login(request,user)
                        return redirect('/')
        else:
            fm = AuhenticatePerson()
            messages.success(request,'Welcome to Yugant Infotech.')
        return render(request,'login_user.html',{'form':fm})
    else:
        return HttpResponseRedirect('/composeEmail/')
        
@api_view(['GET','POST'])
def  logout_person(request):
    logout(request)
    return HttpResponseRedirect('/login/')

        
@api_view(['GET','POST'])
def register(request):
    if not request.user.is_authenticated:
        return render(request,'signupform.html')
    else:
        return HttpResponseRedirect('/composeEmail/')