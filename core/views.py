from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Guest

def landing_page(request):
    return render(request, 'core/landing.html')

def invitation_page(request):
    return render(request, 'core/invitation.html')

def rsvp_page(request):
    query = request.GET.get('q', '')
    guests = None
    if query:
        guests = Guest.objects.filter(name__icontains=query)
    
    return render(request, 'core/rsvp.html', {'guests': guests, 'query': query})

def rsvp_confirm(request, guest_id):
    if request.method == 'POST':
        guest = get_object_or_404(Guest, id=guest_id)
        status = request.POST.get('status')
        if status in ['confirmed', 'declined']:
            guest.status = status
            guest.save()
            messages.success(request, f"Status de {guest.name} atualizado com sucesso!")
        return redirect('rsvp')
    return redirect('rsvp')
