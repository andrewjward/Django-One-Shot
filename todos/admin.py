from django.contrib import admin
from todos.models import TodoLists, TodoItem


# Register your models here.
@admin.register(TodoLists)
class TodoListAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = (
        "task",
        "due_date",
    )
