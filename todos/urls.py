from django.urls import path
from todos.views import todo_list, show_list

urlpatterns = [
    path("", todo_list, name="todo_list_list"),
    path("<int:id>/", show_list, name="todo_list_detail"),
]
