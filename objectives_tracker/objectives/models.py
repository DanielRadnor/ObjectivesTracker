from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=30, unique=True)
    department = models.ForeignKey(Department, null=True, related_name='people', on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Status(models.Model):
    status = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.status

class Task(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, null=True, related_name='tasks', on_delete=models.SET_NULL)
    person = models.ForeignKey(Person, null=True, related_name='tasks', on_delete=models.SET_NULL)
    quadrant = models.IntegerField()
    status = models.ForeignKey(Status, null=True, related_name= 'tasks', on_delete=models.SET_NULL)
    notes = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(Person, null=True, related_name='tasts', on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(Person, null=True, related_name='+', on_delete=models.SET_NULL)

    def __str__(self):
        return self.name