from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('reset_password/', views.reset_password, name='reset_password'),
]

