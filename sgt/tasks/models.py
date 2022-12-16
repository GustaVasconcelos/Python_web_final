from django.db import models

# Create your models here.

class Task(models.Model):
    tarefa = models.TextField(null=False,blank=False)

    def __str__(self) -> str:
        return self.tarefa