from django.shortcuts import render


from rest_framework import viewsets


from rest_framework.permissions import IsAuthenticated


from .models import Task

from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    
    
    queryset =  Task.objects.all()
    
    
    serializer_class = TaskSerializer
    
    permission_classes = [IsAuthenticated]