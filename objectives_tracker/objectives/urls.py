from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='objectives-home'),
    path('home/', views.home, name='objectives-home'),
    path('tasks/', views.tasks, name='objectives-tasks'),
    path('new_task', views.new_task, name='objectives-new-task'),
    path('properties/', views.properties, name='objectives-properties'),
    path('new_property/', views.new_property, name='objectives-new-property'),
    path('categories/', views.categories, name='objectives-categories'),
    path('new_category/', views.new_category, name='objectives-new-category'),
    path('departments/', views.departments, name='objectives-departments'),
    path('new_department/', views.new_department, name='objectives-new-department'),
    path('people/', views.people, name='objectives-people'),
    path('new_person/', views.new_person, name='objectives-new-person'),
    path('statuses/', views.statuses, name='objectives-statuses'),
    path('new_status/', views.new_status, name='objectives-new-status')
]
