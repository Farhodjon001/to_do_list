from django.db import models


# Create your models here.
class Task(models.Model):
    task_name=models.CharField(max_length=500)
    done=models.BooleanField(default=False)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name
 

