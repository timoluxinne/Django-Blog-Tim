from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

# Create your views here.
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, f"Account created successfully! You can now login..")
            form.save()
            return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)

def profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(request.FILES, instance=request.user.profile)
    if request.method == 'POST':
        u_form = UserUpdateForm(request. POST, instance=request.user)
        p_form = ProfileUpdateForm(request.FILES, request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile Updated successfully!")
            return redirect('.')
        
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'accounts/profile.html', context)