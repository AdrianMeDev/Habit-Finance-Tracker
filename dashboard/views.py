from django.shortcuts import render


def dashboard_home(request):
    return render(request, "home.html")


def button_clicked(request):
    return render(request, "button.html")
