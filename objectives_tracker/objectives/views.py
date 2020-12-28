from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Property
from .models import Task
from .models import Department
from .models import Person
from .models import Category
from .models import Status
from .forms import StatusForm

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

def home(request):

    context = {
        'properties': Property.objects.all(),
        'tasks': Task.objects.all(),
        'my_list': ('a', 7, 'xyz', 1),
        'my_variable': "This is my variable"
    }

    return render(request, 'objectives/home.html', context)

def tasks(request):

    context = {
        'tasks': Task.objects.all()
    }

    return render(request, 'objectives/tasks.html', context)

def new_task(request):

    context = {
        'people': Person.objects.all(),
        'quadrant_list': [1,2,3,4],
        'status_list': ["Open","In Progress","Completed","Cancelled"],
        'categories': Category.objects.all()
    }

    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        person = request.POST['person']
        quadrant = request.POST['quadrant']
        status = request.POST['status']
        notes = request.POST['notes']

        task = Task.objects.create(name = name, category_id = category, person_id = person, quadrant = quadrant,
                                   status = status, notes = notes)

        return redirect('objectives-tasks')

    return render(request, 'objectives/new_task.html', context)

def properties(request):

    context = {
        'properties': Property.objects.all()
    }

    return render(request, 'objectives/properties.html', context)

def new_property(request):

    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']

        property = Property.objects.create(name = name, address = address)

        return redirect('objectives-properties')

    return render(request, 'objectives/new_property.html')


def departments(request):

    context = {
        'departments': Department.objects.all()
    }

    return render(request, 'objectives/departments.html', context)

def new_department(request):

    if request.method == 'POST':
        name = request.POST['name']

        department = Department.objects.create(name = name)

        return redirect('objectives-departments')

    return render(request, 'objectives/new_department.html')

def people(request):

    context = {
        'people': Person.objects.all()
    }

    return render(request, 'objectives/people.html', context)

def new_person(request):

    context = {
        'departments': Department.objects.all()
    }

    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']

        person = Person.objects.create(name = name, department_id = department)

        return redirect('objectives-people')

    return render(request, 'objectives/new_person.html', context)

def categories(request):

    context = {
        'categories': Category.objects.all()
    }

    return render(request, 'objectives/categories.html', context)

def new_category(request):

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']

        category = Category.objects.create(name = name, description = description)

        return redirect('objectives-categories')

    return render(request, 'objectives/new_category.html')