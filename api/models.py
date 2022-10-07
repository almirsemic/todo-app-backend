from random import choices
from django.db import models


class Todo(models.Model):
    CHOICES_FIELD = (
        ('Todo', 'Todo'),
        ('In Progress', 'In Progress'),
        ('In Review', 'In Review'),
        ('Done', 'Done')
    )
    author = models.ForeignKey('auth.User', related_name='todo', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=100, choices = CHOICES_FIELD)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    class Meta:
        ordering = ['created_date']
        
