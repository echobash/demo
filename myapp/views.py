from django.shortcuts import render
from .models import TodoItem


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def todo(request):
    items = TodoItem.objects.all()
    return render(request, 'todo.html', {"todos": items})