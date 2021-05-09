from django import forms
from todolist_app.models import TaskList

class TaskForm(forms.ModelForm):
    class Meta:  #contains two models and fields
        model = TaskList
        fields = ['task', 'done']
