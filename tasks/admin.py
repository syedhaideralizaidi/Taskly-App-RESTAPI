from django.contrib import admin

from tasks.models import Task, TaskList


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(TaskList)
class TaskAdmin(admin.ModelAdmin):
    pass

