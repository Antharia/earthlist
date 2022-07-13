from django.contrib import admin
from todos.models import TodoItem

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ("title","commits", "done", "author",)


admin.site.register(TodoItem, TodoItemAdmin)
