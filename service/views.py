from django.shortcuts import render,HttpResponse
from .models import Service, TeamMember
from django.core.mail import send_mail

# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages


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

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send the email
        try:
            send_mail(
                f'Contact Form Message from {name}',  # Subject
                message,  # Message body
                email,  # From email (sender)
                [settings.EMAIL_HOST_USER],  # To email
                fail_silently=False,
            )
            # Optionally, you can use Django messages framework to show a success message
            messages.success(request, 'Thank you for your message! We will get back to you shortly.')
            return redirect('contact')  # Redirect to the same contact page or a success page
        except Exception as e:
            messages.error(request, f"Something went wrong: {str(e)}")

    return render(request, 'contact.html')



