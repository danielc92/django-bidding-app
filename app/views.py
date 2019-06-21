from django.shortcuts import render
from .forms import CustomRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:home')
    else:
        form = CustomRegisterForm()
    
    context = {'form': form}

    return render(request, 'register.html', context)
