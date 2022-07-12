from django.urls import path
from .views import TodoItemListView

urlpatterns = [
    path("", TodoItemListView.as_view(), name="home"),
]
