import requests
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.dispatch import receiver
# from django.db.models.signals import post_save

from . import models

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def menu(request):
    return render(request, 'menu.html', {})


# def contact(request):
#     if request.method == 'POST':
#         Name 		= request.POST.get('Name','')
#         Email 		= request.POST.get('Email','')
#         Contact		= request.POST.get('Contact','')
#         Message 	= request.POST.get('Message','')
#         form_obj 	= models.Contact(name = Name, email = Email, contact = Contact, message = Message)
#         form_obj.save()
#         messages.add_message(request, messages.INFO, f"Thank You.. {Name}")
#     else:
#         messages.add_message(request, messages.INFO, 'Thank You for Giving your Precious Time.')
#     return redirect('/')


# @receiver(post_save,sender=models.Contact)
# def send_sms(sender, created, **kwargs):
#     obj = kwargs['instance']
#     if created and obj.contact != 0:
#         # Sending SMS
#         sms_content = f"Hello, \nSomeone trying to contact you.\nName: {obj.name}\nContact: {obj.contact}\nEmail: {obj.email}\n\nMessage: {obj.message}"

#         my_data = {'sender_id': 'FST2SMS','message': sms_content,'language': 'english','route': 'p','numbers': '7000681073,7415535562'}
#         headers = {'authorization': '6a0iXHGODBECvnVbmSoeYPd5K1Mgl3thUL2zNQp79cJWRfTZFx40eYPvV2SJ1lKXU9Tzp8qGtCsDcuL5',\
#                     'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache"}
#         url = "https://www.fast2sms.com/dev/bulk"
#         requests.request("POST",url,data = my_data,headers = headers)