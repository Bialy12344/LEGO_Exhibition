from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, MocForm, ExhibitionForm, OrganizatorForm
from .models import User, Moc, Exhibition, Organizator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

def home(request):
    return render(request, "exhibitor/home.html", {})

def add_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CustomUserCreationForm()
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
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            user.form.save()
            return redirect("users")
    else:
        form = CustomUserCreationForm(instance=user)
    return render(request, "exhibitor/edit.html", {"form": form})

def add_moc(request):
    if request.method == "POST":
        form = MocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("user_page")
    else:
        form = MocForm()
    return render(request, "exhibitor/add_Moc.html", {"form": form})
@login_required()
def user_page(request):
    mocs = Moc.objects.filter(author=request.user)
    table = Moc.objects.filter(author=request.user).aggregate(Sum('size'))['size__sum'] or 0.00
    return render(request, "exhibitor/user_page.html", {"mocs": mocs, "table": table})

@login_required()
def edit_moc(request, pk):
    moc = Moc.objects.get(pk=pk)
    if request.method == "POST":
        form = MocForm(request.POST, request.FILES, instance=moc)
        if form.is_valid():
            form.save()
            return redirect("user_page")
    else:
        form = MocForm(instance=moc)
    return render(request, "exhibitor/edit_moc.html", {"form": form, "moc": moc})

@login_required()
def delete_moc(request, pk):
    moc = get_object_or_404(Moc, pk=pk)
    if request.method == "POST":
        moc.delete()
        return redirect("user_page")

    return render(request, "exhibitor/confirn.html", {"moc": moc})

def add_exhibition(request):
    if request.method == "POST":
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_page")
    else:
        form = ExhibitionForm()
    return render(request, "exhibitor/add_exhibition.html", {"form": form})

@login_required()
def exhibitions(request):
    exhibitions = Exhibition.objects.all()
    paginator = Paginator(exhibitions, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "exhibitor/exhibitions.html",
        {"page_obj": page_obj},
    )

@login_required()
def organizator(request):
    if request.method == "POST":
        form = OrganizatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_exhibition")
    else:
        form = OrganizatorForm()
    return render(request, "exhibitor/add_organizator.html", {"form": form})
