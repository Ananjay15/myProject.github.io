from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from django.http import *
from .serializers import *
from django.contrib import messages



@api_view(['GET','POST'])
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            serializer = UserSerialisers(data = request.data)
            data = {}
            if serializer.is_valid():
                user = serializer.save()
                print('Information is saved')
                return HttpResponseRedirect('/login/')
            else:
                print('error')
                return HttpResponseRedirect('/sign-up/')
            return HttpResponseRedirect('/sign-up/')
    else:
        return HttpResponseRedirect('/login/')