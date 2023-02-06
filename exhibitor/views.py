from django.shortcuts import render
from .forms import UserForm
def index(request):
    return render(request, 'exhibitor/index.html', {})
def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'exhibitor/index.html', {})
    else:
        form = UserForm()
    return render(request, 'exhibitor/add_user.html', {'form': form})

