from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='home'),
    path('<slug>/', views.detail, name='detail'),
    path('test_drive',views.test_drive, name='test_drive'),

]
