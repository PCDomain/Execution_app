from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'status']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'name', 'description', 'due_date', 'status']