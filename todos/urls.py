from django.urls import path
from todos.views import todo_list, show_list, create_todo_list

urlpatterns = [
    path("", todo_list, name="todo_list_list"),
    path("<int:id>/", show_list, name="todo_list_detail"),
    path("create/", create_todo_list, name="create_list"),
]
