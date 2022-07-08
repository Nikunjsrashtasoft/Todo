#from django.shortcuts import render
from .serializer import Todoserializer ,  Todo_fav_serializer,  todo_is_done_serializer ,Todo_fav_Serializer
from .models import Todo , favourite
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import IntegrityError
from rest_framework.response import Response
from django.contrib.auth import authenticate
# Create your views here.


class TodoListCreate(generics.CreateAPIView):
    serializer_class = Todoserializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by("-created")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class Todo_Upadate_Retrieve_Destory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Todoserializer
    pagination_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


@csrf_exempt
def signup(request):

    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)  # data is a dictionary
            user = User.objects.create_user(
                username=data['username'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)

            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:

            return JsonResponse(
                {'error': 'username taken. choose another username'}, status=400)






@csrf_exempt
def login(request):

    if request.method == 'POST':
        
        try:
            data = JSONParser().parse(request)  # data is a dictionary
            user = authenticate(
                username=data['username'], password=data['password'])
            if user:
            
                return JsonResponse({'message': "login sucess"}, status=200)
            else:
                return JsonResponse({'message': "username or password wrong. choose correct username and password"}, status=400)
        except IntegrityError:

            return JsonResponse(
                {'error': 'invaild data'}, status=400)



class User_isdone_Todo(generics.UpdateAPIView):


    serializer_class = todo_is_done_serializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)
    
    
    def perform_update(self, serializer):
        serializer.instance.is_done = not(serializer.instance.is_done)
        serializer.save()



class User_fav_Todo(generics.UpdateAPIView):


    serializer_class = Todo_fav_serializer
    permission_classes = [permissions.IsAuthenticated]
    if permission_classes:
        # def get_queryset(self):
        #     user = self.request.user
        #     return Todo.objects.filter(user=user)
        def get_queryset(self):
            user = self.request.user
            Todo.objects.filter(user=user)
            return favourite.objects.create(user=user)
        
        
        def perform_update(self, serializer):
            serializer.instance.is_favourite = not(serializer.instance.is_favourite)
            serializer.save()


class fav_Todo_Upadate_Retrieve_Destory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Todo_fav_Serializer
    pagination_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return favourite.objects.filter(user=user)