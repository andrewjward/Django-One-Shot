from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoLists
from todos.forms import TodoListForm


# Create your views here.
def todo_list(request):
    todos = TodoLists.objects.all()
    context = {
        "todo_lists": todos,
    }
    return render(request, "todos/list.html", context)


def show_list(request, id):
    todo = get_object_or_404(TodoLists, id=id)
    context = {
        "list_object": todo,
    }
    return render(request, "todos/detail.html", context)


def create_todo_list(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            created = form.save()
            return redirect("todo_list_detail", id=created.id)
    else:
        form = TodoListForm()
    context = {
        "form": form,
    }
    return render(request, "todos/create.html", context)
