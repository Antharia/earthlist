from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class TodoItem(models.Model):
    title = models.CharField(max_length=140, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    commits = models.PositiveIntegerField(default=0)
    done = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE,
            default="author_name",
            )

    def __str__(self):
        return f"{self.title}: commits {self.commits} done {self.done}"

    def get_rank(self, *args, **kwargs):
        super().save(*args, **kwargs)
        commits = int(self.commits.__str__())
        done = int(self.done.__str__())
        ranking = commits * done
        return ranking


    class Meta:
        ordering = ["done"]
