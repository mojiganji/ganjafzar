
from django.urls import path
from views import views

app_name='accounts'

urlpatterns = [
    path('signup' , views.signup_view , name='signup' ),
]