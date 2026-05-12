from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('convite/', views.invitation_page, name='invitation'),
]
