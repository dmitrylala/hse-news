from django.contrib import admin

from .models import Result, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("num", "timestamp")
    search_fields = ["num"]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("answer", "task")
    search_fields = ["answer"]
