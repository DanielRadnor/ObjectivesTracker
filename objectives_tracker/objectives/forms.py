from django.forms import ModelForm
from .models import Property
from .models import Category
from .models import Department
from .models import Person
from .models import Priority
from .models import Status
from .models import Task

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = "__all__"

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = "__all__"

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = "__all__"
        labels = {
            "status": "Name",
            "description": "Description of Status"
        }

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['property', 'name', 'category', 'person', 'priority', 'status', 'notes']