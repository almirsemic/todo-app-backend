from django.db import models


class Todo(models.Model):
    author = models.ForeignKey('auth.User', related_name='todo', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()

    class Meta:
        ordering = ['created_date']
        
        
    def save(self, *args, **kwargs):
      super().save(*args, **kwargs)
