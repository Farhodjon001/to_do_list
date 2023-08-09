from rest_framework import serializers
from .models import Task

class TaskSerializers(serializers.ModelSerializer):

    class Meta:
        model=Task
        fields=('task_name','done','created_time','updated_time')