from django.shortcuts import render,HttpResponse,redirect
from .models import Service, TeamMember


# views.py
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

#
from twilio.rest import Client
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    services = Service.objects.all()
    team_members = TeamMember.objects.all()
    context = {
        'services': services,
        'teammembers': team_members
    }
    return render(request, 'index.html', context)
# view contact

# def contact(request):
#     return render(request, 'contact.html')
# def contact(request):
#     if request.method == 'POST':
#         # Extract form data
#         name = request.POST.get('name')
#         contact = request.POST.get('contact')
#         message = request.POST.get('message')

#         # Create the SMS message body
#         message_body = f"New Message\nName: {name}\nContact: {contact}\nMessage: {message}"

#         # Send the message using Twilio
#         client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#         try:
#             client.messages.create(
#                 from_=settings.TWILIO_FROM,
#                 body=message_body,
#                 to=settings.SMS_TO,
#             )
#             return HttpResponse("Message sent successfully!")
#         except Exception as e:
#             return HttpResponse(f"Failed to send message: {e}")
#     return render(request, 'contact.html')


def contact(request):
    context = {}
    # default_email="qazisaim121@gmail.com"
    
    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "contact.html", context)

def service_home(request):
    return render(request,'service.html')
def about_home(request):
    return render(request,'about.html')