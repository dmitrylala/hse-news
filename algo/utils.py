from typing import (
    Dict,
    List,
)

from django.db.models import Avg, Max
from django.db.models.query import QuerySet


def format_stat(stat: float) -> str:
    if stat is None:
        return "0.0"
    return f"{stat:.1f}"


def format_stat_percent(stat: float) -> str:
    if stat is None:
        return "0%"
    return f"{stat * 100:.0f}%"


def compute_stats(objects: QuerySet) -> List[Dict[str, str]]:
    return {
        "stats": [
            {
                "value": format_stat(objects.aggregate(Avg("task__num"))["task__num__avg"]),
                "description": "Cpeднee введенное число",
            },
            {
                "value": format_stat(objects.aggregate(Max("task__num"))["task__num__max"]),
                "description": "Maкcимaльнoe введенное число",
            },
        ],
    }


def solve_task(num: float) -> int:
    return (num > 0) - (num < 0)


def sort_options():
    return {
        "sort_options": [
            {
                "field": "task__num",
                "description": "Пo введенному числу",
            },
            {
                "field": "task__timestamp",
                "description": "Пo дате",
            },
        ],
    }


def filter_options():
    return {
        "filter_options": [
            {
                "field": "answer",
                "value": "1",
                "description": "Числа больше нуля",
            },
            {
                "field": "answer",
                "value": "0",
                "description": "Числа, равные нулю",
            },
            {
                "field": "answer",
                "value": "-1",
                "description": "Числа меньше нуля",
            },
        ],
    }
