from django.urls import path , include

#from rest_framework.routers import DefaultRouter
#from app.views import *
from .import views




#router = DefaultRouter()
#router.register(r"Create_Todo/",views.TodoListCreate, basename="TodoListCreate")
#router.register("Todo_Changes/<int:pk>/", views.Todo_Upadate_Retrieve_Destory, basename="Todo_Changes")
# router.register('signup/', views.signup, basename="signup")
# router.register('login/', views.login , basename="login")
# router.register("todo_done/<int:pk>/", views.User_isdone_Todo, basename="todo_done")
# router.register("todo_fav/<int:pk>/", views.User_fav_Todo, basename="todo_fav")
# router.register("todo_fav_delete_update_Retrive/<int:pk>/",views.fav_Todo_Upadate_Retrieve_Destory , basename="todo_fav_delete_update_Retrive")

   
    


urlpatterns = [
    #path("", include(router.urls)),
    path("create_todo/",views.TodoListCreate.as_view()),
    path("todo_changes/<int:pk>/",views.Todo_Upadate_Retrieve_Destory.as_view()),
    path('signup/', views.signup),
    path('login/', views.login),
    path("todo_done/<int:pk>/",views.User_isdone_Todo.as_view()),
    path("todo_fav/<int:pk>/",views.User_fav_Todo.as_view()),
    path("todo_fav_delete_update_Retrive/<int:pk>/",views.fav_Todo_Upadate_Retrieve_Destory.as_view()),
 
]


