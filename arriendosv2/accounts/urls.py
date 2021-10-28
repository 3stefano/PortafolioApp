from django.urls import path
from . import views
from django.contrib.auth.views import logout_then_login



urlpatterns = [
    path('', views.home, name = 'home'),
    path('propiedades/', views.propiedades, name='propiedades'),
    path('reserva/', views.reserva, name='reserva'),
    path('checkin/<searched>', views.checkin,name='checkin'),
    path('checkout/', views.checkout,name='checkout'),
    path('adminapp/', views.adminapp,name='adminapp'),
    path('accounts/login/', views.loginpage,name='loginpage'),
    path('logout/', logout_then_login, name = 'logout'),
    path('busqueda_reserva/', views.busqueda_reserva, name='busqueda_reserva'),
    path('delete_reserva/<searched>', views.delete_reserva, name='delete_reserva'),
    path('pago/<searched>', views.pago,name='pago'),
    path('agregar_pago/<searched>', views.agregar_pago, name='agregar_pago'),



]


