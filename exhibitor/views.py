from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Create your views here.


def index(request):
    return render(request, "exhibitor/index.html", {})


def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UserForm()
    return render(request, "exhibitor/add_user.html", {"form": form})


def users(request):
    users = User.objects.filter(is_active=True)
    paginator = Paginator(users, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "exhibitor/users.html",
        {"page_obj": page_obj},
    )


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
