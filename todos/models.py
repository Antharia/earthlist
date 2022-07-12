from django.db import models
from django.urls import reverse


class TodoItem(models.Model):
    title = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now_add=True)
    commits = models.IntegerField()
    done = models.IntegerField()

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title}: commits {self.commits} done {self.done}"

    class Meta:
        ordering = ["commits"]
