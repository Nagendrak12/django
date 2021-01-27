from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from todo.models import Todo
from todo.serializers import TodoSerializer


@api_view(['GET', 'POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes( [IsAuthenticated])
def todos(request):
    if request.method == "GET":
        todos = Todo.objects.all().order_by('-addedon')
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    else:  # Post
        serializer = TodoSerializer(data=request.data)  # Convert JSON to Todo
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def todo_details(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'PUT':  # Update
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update table in DB
            return Response(serializer.data)
        else:
            # Bad request
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:  # Delete
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
