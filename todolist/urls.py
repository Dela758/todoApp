from django.urls import path
from . import views

urlpatterns = [
    # Path for homepage
    path('', views.index, name='index'),
    # Path for form
    path('add', views.addTodoItem, name='add'),
    # Path for completed
    path('completed/<todo_id>', views.completedTodo, name='completed'),
    # Path to delete all completed items
    path('deletecompleted', views.deleteCompleted, name='deletecompleted'),
    # Path to delete all items
    path('deleteAll', views.deleteAll, name='deleteAll')

]