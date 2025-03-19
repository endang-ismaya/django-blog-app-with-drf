from django.shortcuts import render

# Create your views here.

def index(request):
    """author index view"""
    context = {}
    return render(request, "author/index.html", context)
