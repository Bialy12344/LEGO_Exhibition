from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def index(request):
    return render(request, "exhibitor/index.html", {})


def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("index")
    else:
        form = UserForm()
    return render(request, "exhibitor/add_user.html", {"form": form})
def users(request):
    users = User.objects.filter(is_active=True)
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "exhibitor/users.html", {"page_obj": page_obj}, )
