from django.urls import path
from todolist.views import logout_user, show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout
from todolist.views import create_task
from todolist.views import change_status
from todolist.views import delete_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create_task'),
    path('change-status/', change_status, name='change_status'),
    path('delete-task/', delete_task, name='delete_task'),
]