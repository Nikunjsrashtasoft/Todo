from django.urls import path
from .import views 

urlpatterns = [

path("Create_Todo/",views.TodoListCreate.as_view()),
path("Todo_Changes/<int:pk>/",views.Todo_Upadate_Retrieve_Destory.as_view()),
path('signup/', views.signup),
path('login/', views.login),
path("todo_done/<int:pk>/",views.User_isdone_Todo.as_view()),
path("todo_fav/<int:pk>/",views.User_fav_Todo.as_view()),
path("todo_fav_delete_update_Retrive/<int:pk>/",views.fav_Todo_Upadate_Retrieve_Destory.as_view()),

]