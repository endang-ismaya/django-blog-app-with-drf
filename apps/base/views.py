from django.shortcuts import render

# Create your views here.

def index(request):
    """base index view"""
    context = {}
    return render(request, "base/index.html", context)
