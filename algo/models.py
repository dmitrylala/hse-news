from django.db import models


class Task(models.Model):
    num = models.FloatField("Число")

    timestamp = models.DateTimeField("Время", auto_now=True)

    def __str__(self):
        return f"number = {self.num}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Result(models.Model):
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Задача",
    )

    answer = models.IntegerField("Ответ")

    def __str__(self):
        return f"Answer: number is {self.answer}, task: {self.task}"

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"
