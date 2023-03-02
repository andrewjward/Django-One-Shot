from django.forms import ModelForm
from todos.models import TodoLists, TodoItem


class TodoListForm(ModelForm):
    class Meta:
        model = TodoLists
        fields = [
            "name",
        ]


class TodoItemForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = [
            "task",
            "due_date",
            "is_completed",
            "list",
        ]
