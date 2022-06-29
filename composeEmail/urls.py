from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'composeEmail'

urlpatterns = [
 
    path('composeEmail/' , views.mailsending , name='mailSending' ),
    path('',views.index,name='home'),
    path('sent_box/',views.sent_box, name='send_box'),
    path('delete_sent_mail/<int:pk>/',views.delete_sent_mail,name='delete_sent_mail'),
    path('delete/',views.delete_row,name='delete_mail'),
]