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
from .models import Priority
from .forms import PriorityForm
from .models import Status
from .forms import StatusForm
from .models import Task
from .forms import TaskForm
from .filters import TaskFilter

from django.template.defaulttags import register

def home(request):

    tasks = Task.objects.all()

    total_tasks = 0
    total_tasks_p1 = 0
    total_tasks_p2 = 0
    total_tasks_p3 = 0
    total_tasks_p4 = 0

    for task in tasks:

        total_tasks += 1
        if task.priority.name == "1":
            total_tasks_p1 += 1
        elif task.priority.name == "2":
            total_tasks_p2 += 1
        elif task.priority.name == "3":
            total_tasks_p3 += 1
        else:
            total_tasks_p4 += 1

    properties = Property.objects.all()
    prop_task_dict = {}
    prop_task_count = 0

    for property in properties:
        prop_task_count = 0
        prop_task_dict[property.name] = 0
        for task in tasks:
            if task.property == property:
                prop_task_count += 1
                prop_task_dict[property.name] = prop_task_count

    @register.filter
    def calculate_something(a, b):
        return a + b

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    context = {
        'properties': properties,
        'tasks': tasks,
        'total_tasks': total_tasks,
        'total_tasks_p1': total_tasks_p1,
        'total_tasks_p2': total_tasks_p2,
        'total_tasks_p3': total_tasks_p3,
        'total_tasks_p4': total_tasks_p4,
        'prop_task_dict': prop_task_dict
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

def delete_property(request, pk):

    property = Property.objects.get(id=pk)

    if request.method == 'POST':
        property.delete()
        messages.success(request, "Property successfully deleted!")
        return redirect('objectives-properties')

    context = {
        'item': property
    }

    return render(request, 'objectives/delete_property.html', context)

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

def delete_category(request, pk):

    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        category.delete()
        messages.success(request, "Category successfully deleted!")
        return redirect('objectives-categories')

    context = {
        'item': category
    }

    return render(request, 'objectives/delete_category.html', context)

def departments(request):

    departments = Department.objects.all()

    context = {
        'departments': departments
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

    return render(request, 'objectives/new_department.html',context)

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

def delete_department(request, pk):

    department = Department.objects.get(id=pk)

    if request.method == 'POST':
        department.delete()
        messages.success(request, "Department successfully deleted!")
        return redirect('objectives-departments')

    context = {
        'item': department
    }

    return render(request, 'objectives/delete_department.html', context)

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

    #return render(request, 'objectives/new_person.html', context)

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

def delete_person(request, pk):

    person = Person.objects.get(id=pk)

    if request.method == 'POST':
        person.delete()
        messages.success(request, "Person successfully deleted!")
        return redirect('objectives-people')

    context = {
        'item': person
    }

    return render(request, 'objectives/delete_person.html', context)

def priorities(request):

    context = {
        'priorities': Priority.objects.all()
    }

    return render(request, 'objectives/priorities.html', context)

def new_priority(request):

    form = PriorityForm()
    if request.method == 'POST':
        form = PriorityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objectives-priorities')

    context = {
        'form': form
    }

    return render(request, 'objectives/new_priority.html', context)

def update_priority(request, pk):

    priority = Priority.objects.get(id=pk)
    form = PriorityForm(instance=priority)

    if request.method == 'POST':
        form = PriorityForm(request.POST,instance=priority)
        if form.is_valid():
            form.save()
            return redirect('objectives-priorities')

    context = {
        'form': form
    }

    return render(request, 'objectives/update_priority.html', context)

def delete_priority(request, pk):

    priority = Priority.objects.get(id=pk)

    if request.method == 'POST':
        priority.delete()
        messages.success(request, "Priority successfully deleted!")
        return redirect('objectives-proprities')

    context = {
        'item': priority
    }

    return render(request, 'objectives/delete_priority.html', context)

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

def delete_status(request, pk):

    print("request:", request)
    print("pk:", pk)

    status = Status.objects.get(id=pk)

    if request.method == 'POST':
        status.delete()
        messages.success(request, "Status successfully deleted!")
        return redirect('objectives-statuses')

    context = {
        'item': status
    }

    print("context:", context)

    return render(request, 'objectives/delete_status.html', context)

def tasks(request):

    tasks = Task.objects.all()
    people = Person.objects.all()
    categories = Category.objects.all()

    task_filter = TaskFilter(request.GET, queryset=tasks)

    tasks = task_filter.qs

    context = {
        'tasks': tasks,
        'people': people,
        'categories': categories,
        'task_filter': task_filter
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

    return render(request, 'objectives/delete_task.html', context)