import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AccountRegistrationForm

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        redirect('/')
    
    if request.method == 'POST':
        accountform = AccountRegistrationForm(request.POST)
        if accountform.is_valid():
            user = accountform.save(commit=True)
            user.email = accountform.cleaned_data['username']

            user.set_password(accountform.cleaned_data['password'])
            user.save()
            response = redirect('/quizhome/')
            return response

    else:
        accountform = AccountRegistrationForm()
    return render(request, 'users/register.html', {'form':accountform})






