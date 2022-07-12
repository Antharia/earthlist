from django.views.generic import ListView
from .models import TodoItem


class TodoItemListView(ListView):
    model = TodoItem
    template_name = "home.html"
