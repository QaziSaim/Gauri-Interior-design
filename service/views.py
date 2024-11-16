from django.shortcuts import render
from .models import Service, TeamMember


# Create your views here.
def index(request):
    services = Service.objects.all()
    team_members = TeamMember.objects.all()
    context = {
        'services': services,
        'teammembers': team_members
    }
    return render(request, 'index.html', context)

def contact_view(request):
    pass