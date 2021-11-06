from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class Status (models.Model):
    status_name = models.CharField(max_length=20)

    def __str__(self):
        return self.status_name


class Task (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=2)
    text = models.TextField('Task')


    def __str__(self):
        return self.text


class Answer (models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='answer')
    text = models.TextField('Answer')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children'
    )

    def __str__(self):
        return self.text