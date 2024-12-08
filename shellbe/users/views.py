from django.shortcuts import render
from users.forms import UserCreateform1
# Create your views here.

def registor_view(request):
    form = None
    if request.method=="POST":
    
       form = UserCreateform1(request.POST)
       
       if form.is_valid():
           form.save()
       else:
           form = UserCreateform1
            
    
    return render(request,'registor.html',{'form':form})