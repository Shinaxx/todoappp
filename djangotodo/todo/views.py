from django.shortcuts import render

from .models import Todo


def todos(request):
    todos = Todo.objects.all()

    return render(request, 'todos.html', {'todos': todos})

