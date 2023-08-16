from django.urls import path
from tasks.views import home,add_task,view_task,completed_task
urlpatterns = [
    path('',home,name="home"),
    path('add_task/',add_task,name="add_task"),
    path('view_task/',view_task,name="view_task"),
    path('completed_task/',completed_task,name="completed_task"),
]
