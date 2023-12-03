
from django.urls import path
from django.contrib.auth.forms import views

app_name='accounts'

urlpatterns = [
    path('signup' , views.signup_view , name='signup' ),
]