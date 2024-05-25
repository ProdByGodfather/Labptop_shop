from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.forms import UserEditForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required(login_url=reverse_lazy('login'))
def dashboard(request):
    if request.method == 'POST': 
        form = UserEditForm(request.POST, instance=request.user) 
        if form.is_valid(): 
            form.save() 
            return redirect('home')  
    else: 
        form = UserEditForm(instance=request.user) 

    return render(request, 'registration/edit_user.html', {'form': form}) 
 