from django.urls import path
from tasks.views import home,add_task,show_tasks,completed_task,edit_task,delete_task,complete_task,repriotise_task
urlpatterns = [
    path('',home,name="home"),
    path('add_task/',add_task,name="add_task"),
    path('show_tasks/',show_tasks,name="show_tasks"),
    path('completed_task/',completed_task,name="completed_task"),
    path('edit_task/<int:id>',edit_task,name="edit_task"),
    path('delete_task/<int:id>',delete_task,name="delete_task"),
    path('complete_task/<int:id>',complete_task,name="complete_task"),
    path('repriotise_task/<int:id>',repriotise_task,name="repriotise_task"),
]
