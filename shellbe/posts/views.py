from django.shortcuts import render
from posts.forms import Postform
# Create your views here.

def createposts_view(request):
    formpost = None
    
    if request.method=="POST":
        
        formpost = Postform(request.POST)
        
        if formpost.is_valid():
            formpost.save()
            
    else:
        formpost = Postform()
        
    return render(request,'createpost.html',{'formpost':formpost})