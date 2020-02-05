from django.shortcuts import render


def index(request):
    return render(request, "Nomina/_index.html", {"titulo": "Dashboard"})