from django.shortcuts import render

def landing_page(request):
    return render(request, 'core/landing.html')

def invitation_page(request):
    return render(request, 'core/invitation.html')
