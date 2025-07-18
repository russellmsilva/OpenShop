from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

# Accept POST requests to /logout/ but deny GET requests with HTTP 404 error
@method_decorator(login_required, name='dispatch')
class SecureLogoutView(View):
    def get(self, request):
        # Explicitly block direct URL access
        raise Http404("Page not found")

    def post(self, request):
        logout(request)
        return redirect('login')
    