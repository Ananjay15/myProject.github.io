from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import *
from django.http import HttpResponseRedirect
from accounts.models import Registry, Save_Mail, Attachment
from django.contrib.auth.models  import  User
import base64
import datetime
from imap_tools import MailBox, AND, OR
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib import messages
from django.core.mail import EmailMessage
import mimetypes
import os, shutil, errno
import traceback
import codecs
from datetime import date

EMAIL_HOST_USER = getattr(settings ,'EMAIL_HOST_USER')

data = {}


@api_view(['GET','POST'])
def mailsending(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            to = request.data['to']
            cc = request.data['cc']
            password = ''
            reg = Registry.objects.filter(email=request.user.username)

            for item in reg:
                password = item.password

            base64_bytes = password.encode("ascii")
            sample_string_bytes = base64.b64decode(base64_bytes)
            pwd = sample_string_bytes.decode("ascii")

            
            l = []
            l.append(to)
            to_tuple = tuple(l)
            c = []
            c.append(cc)
            print(c)
            email = EmailMessage(subject=request.data['Subject'],body=request.data['body'],from_email=request.user.username,to=to_tuple,cc=c)
            email.content_subtype = 'html'
            data = request.FILES.getlist('files')
            for files in request.FILES.getlist('files'):
                email.attach(files.name,files.read(),files.content_type)

            email.send()
            save_mail = Save_Mail(email=request.user.username,to=request.data['to'],subject=request.data['Subject'],message=request.data['body'])
            save_mail.save()  
            files = request.FILES.getlist('files')
            for files in files:
                attach = Attachment(email=save_mail,files=files)
                attach.save()

            return redirect('composeEmail:send_box')
        else:
            
            users = Registry.objects.all()
            print(users)
            user_ = User.objects.filter(username=request.user.username)
            for name in user_:
                email = name.email
                join_date = name.date_joined
                status = name.is_active

            print(join_date.date())
            valid = int((date.today() - join_date.date()).days)
            print(valid)
            validity = 365 - valid
            return render(request, 'mailSending/composeEmail.html',{'validity':validity})
    else:
        return HttpResponseRedirect('/login/')




def delete_sent_mail(request,pk):
    if request.user.is_authenticated:
        msg = Save_Mail.objects.get(pk=pk)
        msg.delete()
        return HttpResponseRedirect('/sent_box/')
    else:
        return HttpResponseRedirect('/sent_box/')


def delete_row(request):
    if request.method == 'POST':
        getdata = request.POST.getlist('mail')
        print(getdata)
        for data in getdata:
            msg = Save_Mail.objects.get(pk=data)
            msg.delete()
        return HttpResponseRedirect('/sent_box/')
    else:
        return HttpResponseRedirect('/send_box/')


'''
def receive_gmail(username,password):
    mailbox = MailBox('imap.gmail.com')
    mailbox.login(username, password, initial_folder='INBOX') 
    return mailbox.fetch(AND(all=True),reverse=True)
'''

def search_mail(username,password,text):
    mailbox = MailBox('imap.gmail.com')
    mailbox.login(username, password, initial_folder='INBOX')
    print(mailbox.folder.get()) 
    return mailbox.fetch(OR(text=text), charset='utf8',reverse=True)


def receive_gmail(username,password):

    mailbox = MailBox('imap.gmail.com')
    mailbox.login(username, password, initial_folder='INBOX') 
    # mailbox.fetch(AND(all=True),reverse=True)
    for msg in mailbox.fetch():
        for att in msg.attachments:
            print(att.filename, att.content_type)
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(att.filename)))
            print(BASE_DIR + "\\api\\static\\userDoc\\{}")
            with open(BASE_DIR + "\\api\\static\\userDoc\\{}".format(att.filename), 'wb') as f:
                f.write(att.payload)  
    return mailbox.fetch(AND(all=True),reverse=True)



def sent_box(request):
    if request.user.is_authenticated:
        user_ = User.objects.filter(username=request.user.username)
        for name in user_:
            email = name.email
            join_date = name.date_joined
            status = name.is_active

        print(join_date.date())
        valid = int((date.today() - join_date.date()).days)
        print(valid)
        validity = 365 - valid
        
        msg = Save_Mail.objects.filter(email=request.user.username).order_by('-id')
        return render(request,'sent_mail.html',{'msg':msg,'validity':validity})

    else:
        return HttpResponseRedirect('/login/')


def search_in_mail_box(request):
    data = request.POST.get('search')
    print(data)
    return HttpResponseRedirect('/sent_box/')


@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        print(request.POST['user'])
        password = ''
        reg = Registry.objects.filter(email=request.user.username)
        print(reg)
        for item in reg:    
            password = item.password
        print(password)
        base64_bytes = password.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        pwd = sample_string_bytes.decode("ascii")
        print(request.user.username)
        print(pwd)

        msg = search_mail(request.user.username,pwd,request.POST['user'])

        return render(request,'mailSending/home.html',{'msg':msg})
    else:
        password = ''
        reg = Registry.objects.filter(email=request.user.username)

        for item in reg:
            password = item.password

        base64_bytes = password.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        pwd = sample_string_bytes.decode("ascii")

        print(request.user.id)
        users = Registry.objects.all()
        user_ = User.objects.filter(username=request.user.username)
        for name in user_:
            email = name.email
            join_date = name.date_joined
            status = name.is_active

        print(join_date.date())
        valid = int((date.today() - join_date.date()).days)
        print(valid)
        validity = 365 - valid
        msg = receive_gmail(request.user.username,pwd)
        return render(request,'mailSending/home.html',{'msg':msg,'validity':validity})