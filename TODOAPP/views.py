from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Todo

#Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls={
		'List':'/task-list/',
		'Detail View' :'/task-details/<str:pk>/',
		'Create' :'task-create',
		'Update' :'/task-update/<str:pk>/',
		'Delete' :'task-delete/<str:pk>/',
	}
	return Response(api_urls)


@api_view(['GET'])
def taskList(request):
	tasks = Todo.objects.all()
	serializer = TaskSerializer(tasks,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetails(request,pk):
	tasks = Todo.objects.get(id=pk)
	serializer = TaskSerializer(tasks,many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request,pk):
	task=Todo.objects.get(id=pk)
	serializer=TaskSerializer(instance=task,data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request,pk):
	tasks = Todo.objects.get(id=pk)
	tasks.delete()
	return Response("Task Successfully Deleted")
