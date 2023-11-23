from django.shortcuts import render
from forms import UserCreationForm
# Create your views here.
def signup_view(request):
    form=UserCreationForm()
    return render(request , 'signup.html' , {'form':form})
