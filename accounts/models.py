from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Registry(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length = 150,default=None)
    phone = models.CharField(max_length=12,default=None)
    date = models.DateTimeField(default=datetime.now())
    is_active = models.BooleanField(default=True)
    pending = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Save_Mail(models.Model):
    email = models.EmailField(max_length=250)
    to = models.CharField(max_length = 150)
    subject = models.CharField(max_length = 150)
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.email


class Attachment(models.Model):
    email = models.ForeignKey(Save_Mail, on_delete=models.CASCADE,related_name='attach')
    files = models.FileField(upload_to='media/', max_length = 100)
    date = models.DateTimeField(default=datetime.now())
    





    