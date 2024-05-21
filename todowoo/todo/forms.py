from django.forms import ModelForm
from .models import Todo

#Форма создания задачи (из модели) и вывода необходимых полей в данную форму
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']
