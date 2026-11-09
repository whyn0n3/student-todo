"""Терминальное меню менеджера задач студенческой группы."""

from tasks import TaskManager


def main() -> None:
    manager = TaskManager()
    print("Менеджер задач студенческой группы")
    print("На этом этапе задачи хранятся только до выхода из программы.")

    while True:
        print("\n1. Показать задачи")
        print("2. Добавить задачу")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()
