from django.views.generic import ListView
from .models import TodoItem


class TodoItemListView(ListView):
    model = TodoItem
    context_object_name = "todoitem_list"
    template_name = "home.html"
