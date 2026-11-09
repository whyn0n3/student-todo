"""Задачи и операции с ними. Этот модуль не зависит от терминала."""

from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str


class TaskManager:
    def __init__(self) -> None:
        self._tasks: list[Task] = []
        self._next_id = 1

    def add_task(self, title: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("Название задачи не может быть пустым.")

        task = Task(id=self._next_id, title=title)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self) -> list[Task]:
        return self._tasks.copy()
