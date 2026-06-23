from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('convite/', views.invitation_page, name='invitation'),
    path('confirmar-presenca/', views.rsvp_page, name='rsvp'),
    path('confirmar-presenca/<int:guest_id>/', views.rsvp_confirm, name='rsvp_confirm'),
    path('lista-de-presentes/', views.gift_list_page, name='gift_list'),
    path('lista-de-presentes/escolher/<int:gift_id>/', views.choose_gift, name='choose_gift'),
]
