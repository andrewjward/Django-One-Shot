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


def edit_todo_list(request, id):
    post = get_object_or_404(TodoLists, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=post)
        if form.is_valid():
            edit = form.save()
            return redirect("todo_list_detail", id=edit.id)
    else:
        form = TodoListForm(instance=post)
    context = {
        "edit_object": post,
        "form": form,
    }
    return render(request, "todos/edit.html", context)


def delete_todo_list(request, id):
    delete = TodoLists.objects.get(id=id)
    if request.method == "POST":
        delete.delete()
        return redirect("todo_list_list")
    return render(request, "todos/delete.html")
