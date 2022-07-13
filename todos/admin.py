from django.contrib import admin
from todos.models import TodoItem

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ("title","commits", "done",)


admin.site.register(TodoItem, TodoItemAdmin)
