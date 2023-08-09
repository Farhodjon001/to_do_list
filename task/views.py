from django.shortcuts import render
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Task
from rest_framework import generics
# Create your views here.

class TaskListApiView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
class TaskDetailApiView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
class TaskCreateApiView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
class TaskUpdateApiView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
class TaskDeleteApiView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

