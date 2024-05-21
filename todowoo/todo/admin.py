from django.contrib import admin
from .models import Todo

#Кастомизация панели администратора (чтобы отображалась дата создания)
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

#Отображение задач в панели администратора
admin.site.register(Todo, TodoAdmin)
