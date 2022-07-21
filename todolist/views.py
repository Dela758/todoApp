from django.shortcuts import redirect, render

from todolist.forms import TodoListForm

from .models import Todolist

from .forms import TodoListForm

from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_items = Todolist.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items' : todo_items, 'form' : form}
    return render(request, 'todolist/index.html', context)

# View for adding form input to database
@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)

    if form.is_valid():
        new_todo = Todolist(text = request.POST['text'])
        new_todo.save()

    return redirect('index')

# View for completed items
def completedTodo(request, todo_id):
    # Query database for specific todo_id 
    todo = Todolist.objects.get(pk = todo_id)
    # Update database by setting value to true
    todo.completed = True
    # Save changes
    todo.save()

    return redirect('index')

# View to delete completed items
def deleteCompleted(request):
    # Query database for all items marked as completed and delete
    Todolist.objects.filter(completed__exact=True).delete()

    return redirect('index')

# View to delete all items
def deleteAll(request):
    # Query the database for all items and call the delete method
    Todolist.objects.all().delete()

    return redirect('index')