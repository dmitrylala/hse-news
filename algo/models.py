from django.db import models


class Task(models.Model):
    num = models.FloatField()

    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"number = {self.num}"


class Result(models.Model):
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    answer = models.IntegerField()

    def __str__(self):
        return f"Answer: number is {self.answer}, task: {self.task}"
