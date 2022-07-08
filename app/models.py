from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    todo_title = models.CharField(max_length=200)
    todo_description = models.TextField(blank=True ,null=True)
    is_done = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo_title

class favourite(models.Model):
    #todo=models.ForeignKey(Todo, on_delete=models.CASCADE)
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    is_favourite=models.BooleanField(default=False)