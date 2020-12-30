from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Property
from .forms import PropertyForm
from .models import Category
from .forms import CategoryForm
from .models import Department
from .forms import DepartmentForm
from .models import Person
from .forms import PersonForm
from .models import Status
from .forms import StatusForm
from .models import Task
from .forms import TaskForm

def home(request):

    context = {
        'properties': Property.objects.all(),
        'tasks': Task.objects.all(),
        'my_list': ['a', 7, 'xyz', 1],
        'my_variable': "This is my variable"
    }

    return render(request, 'objectives/home.html', context)

def properties(request):

    context = {
        'properties': Property.objects.all()
    }

    return render(request, 'objectives/properties.html', context)

def new_property(request):
    form = PropertyForm

    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objectives-properties')

    context = {
        'form': form
    }

    return render(request, 'objectives/new_property.html', context)

def update_property(request, pk):

    property = Property.objects.get(id=pk)
    form = PropertyForm(instance=property)

    if request.method == 'POST':
        form = PropertyForm(request.POST,instance=property)
        if form.is_valid():
            form.save()
            return redirect('objectives-properties')

    context = {
        'form': form
    }

    return render(request, 'objectives/update_property.html', context)

def categories(request):

    context = {
        'categories': Category.objects.all()
    }

    return render(request, 'objectives/categories.html', context)

def new_category(request):

    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objectives-categories')

    context = {
        'form': form
    }

    return render(request, 'objectives/new_category.html', context)

def update_category(request, pk):

    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('objectives-categories')

    context = {
        'form': form
    }

    return render(request, 'objectives/update_category.html', context)

def departments(request):

    context = {
        'departments': Department.objects.all()
    }

    return render(request, 'objectives/departments.html', context)

def new_department(request):

    form = DepartmentForm()

    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objectives-departments')

    context = {
        'form': form
    }

    return render(request, 'objectives/new_department.html')

def update_department(request, pk):

    department = Department.objects.get(id=pk)
    form = DepartmentForm(instance=department)

    if request.method == 'POST':
        form = DepartmentForm(request.POST,instance=department)
        if form.is_valid():
            form.save()
            return redirect('objectives-departments')

    context = {
        'form': form
    }

    return render(request, 'objectives/update_department.html', context)

def people(request):

    context = {
        'people': Person.objects.all()
    }

    return render(request, 'objectives/people.html', context)

def new_person(request):

    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objectives-people')

    context = {
        'form': form,
        'departments': Department.objects.all()
    }

    return render(request, 'objectives/new_person.html', context)

    '''
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']

        person = Person.objects.create(name = name, department_id = department)

        return redirect('objectives-people')

    '''

    return render(request, 'objectives/new_person.html', context)

def update_person(request, pk):

    person = Person.objects.get(id=pk)
    form = PersonForm(instance=person)

    if request.method == 'POST':
        form = PersonForm(request.POST,instance=person)
        if form.is_valid():
            form.save()
            return redirect('objectives-people')

    context = {
        'form': form
    }

    return render(request, 'objectives/update_person.html', context)

def statuses(request):
    context = {
        'statuses': Status.objects.all()
    }

    return render(request, 'objectives/statuses.html', context)

def new_status(request):
    form = StatusForm()
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objectives-statuses')

    context = {'form': form}

    return render(request, 'objectives/new_status.html', context)

def update_status(request, pk):

    status = Status.objects.get(id=pk)
    form = StatusForm(instance=status)

    if request.method == 'POST':
        form = StatusForm(request.POST,instance=status)
        if form.is_valid():
            form.save()
            return redirect('objectives-statuses')

    context = {
        'form': form
    }

    return render(request, 'objectives/update_status.html', context)

def tasks(request):

    context = {
        'tasks': Task.objects.all()
    }

    return render(request, 'objectives/tasks.html', context)

# Need to work on this so that it correctly takes into account the related models.

def new_task(request):

    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New task successfully created!")
            return redirect('objectives-tasks')

    '''
        name = request.POST['name']
        category = request.POST['category']
        person = request.POST['person']
        quadrant = request.POST['quadrant']
        status = request.POST['status']
        notes = request.POST['notes']
        
        task = Task.objects.create(name = name, category_id = category, person_id = person, quadrant = quadrant,
                                   status = status, notes = notes)
        

    context = {
        'form': form,
        'people': Person.objects.all(),
        'quadrant_list': [1,2,3,4],
        'status_list': ["Open","In Progress","Completed","Cancelled"],
        'categories': Category.objects.all()
    }
    '''

    context = {
        'form': form
    }

    return render(request, 'objectives/new_task.html', context)

def update_task(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task successfully updated!")
            return redirect('objectives-tasks')

    context = {
        'form': form
    }

    return render(request, 'objectives/update_task.html', context)

def delete_task(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task successfully deleted!")
        return redirect('objectives-tasks')

    context = {
        'item': task
    }

    return render(request, 'objectives/delete.html', context)