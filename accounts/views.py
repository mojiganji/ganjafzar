from django.shortcuts import render
from accounts.forms import UserCreationForm
# Create your views here.
def signup_view(request):
    form=UserCreationForm()
    return render(request , 'accounts/signup.html' , {'form':form})
