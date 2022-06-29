from django.contrib import admin
from .models import *

class AdminRegistry(admin.ModelAdmin):
    list_display = ('name','email','phone','date','is_active','pending')
    search_fields = ['name','email','phone','date','is_active','pending']

class AdminAttach(admin.ModelAdmin):
    list_display = ('email','files','date')
    search_fields = ['email','files','date']

class AdminSaveMail(admin.ModelAdmin):
    list_display = ('email','to','date')
    search_fields = ['email','to','date']




admin.site.register(Registry,AdminRegistry)

admin.site.register(Attachment,AdminAttach)
admin.site.register(Save_Mail,AdminSaveMail)