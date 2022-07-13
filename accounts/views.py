from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import CustomUserCreationForm
from .models import CustomUser
from todos.models import TodoItem

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def dashboard_view(request):
    author = request.user.username
    todo_item_list = TodoItem.objects.filter(author__username=author)
    context = {"todo_item_list": todo_item_list}
    return render(request, "dashboard.html", context)

