from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import CUser

def registor(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')  # Get the uploaded file

        
        user = CUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            phone_number=phone_number,
            password=make_password(password),  # Hash the password
            user_profile=profile_pic  # Save the profile picture
        )
        user.save()

          # Replace 'success_url' with your success page
    return render(request, 'registor.html')


