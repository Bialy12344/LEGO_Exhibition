from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "exhibitor/home.html", {})

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserForm()
    return render(request, "exhibitor/add_user.html", {"form": form})

@login_required()
def users(request):
    users = User.objects.all()
    paginator = Paginator(users, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "exhibitor/users.html",
        {"page_obj": page_obj},
    )

@login_required()
def edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("users")
    else:
        form = UserForm(instance=user)
    return render(request, "exhibitor/edit.html", {"form": form})
@login_required()
def user_page(request):
    return render(request, "exhibitor/user_page.html",  {})