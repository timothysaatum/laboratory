from django.shortcuts import render, redirect
from .forms import SignUp

def sign_up(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUp()
    return render(request, 'users/register.html', {'form':form})
#
#form to be displayed for hospitals to create account
#def hospital_sign_up(request):
#    if request.method == 'POST':
#        form = HospitalSignUp(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#    else:
#        form = HospitalSignUp()
#    return render(request, 'users/hospital.html', {'form':form})
#
#
#def delivery_sign_up(request):
#    if request.method == 'POST':
#        form = DeliverySingUP(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#    else:
#       form = DeliverySingUP()
#    return render(request, 'users/delivery.html', {'form':form})