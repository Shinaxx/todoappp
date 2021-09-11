from django.urls import path

from djangotodo.todo import views

urlpatterns = [
    path('',views.todos, name='todos'),
]
