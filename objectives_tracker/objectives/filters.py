import django_filters
from .models import *

class TaskFilter(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = ['property', 'person', 'person__department', 'priority', 'status']