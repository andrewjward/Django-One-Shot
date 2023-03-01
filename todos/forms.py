from django.forms import ModelForm
from todos.models import TodoLists


class TodoListForm(ModelForm):
    class Meta:
        model = TodoLists
        fields = [
            "name",
        ]
