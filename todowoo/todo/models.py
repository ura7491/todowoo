from django.db import models
from django.contrib.auth.models import User

#Модель создания задачи
class Todo(models.Model):
    #Заголовок
    title = models.CharField(max_length=100)

    #Описание
    memo = models.TextField(blank=True)

    #Дата создания
    created = models.DateTimeField(auto_now_add=True)

    #Дата завершения
    datecompleted = models.DateTimeField(null=True, blank=True)

    #Важная задача
    important = models.BooleanField(default=False)

    #Пользователь задачи
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
