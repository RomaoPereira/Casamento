from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('convite/', views.invitation_page, name='invitation'),
    path('confirmar-presenca/', views.rsvp_page, name='rsvp'),
    path('confirmar-presenca/<int:guest_id>/', views.rsvp_confirm, name='rsvp_confirm'),
]
