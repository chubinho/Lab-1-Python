from typing import Any
from task import Task


class APIMockSource:
    """
    Источник задач, имитирующий внешний API
    """
    def __init__(self, tasks_data: list[dict[str, Any]] | None = None) -> None:
        """
        Инициализация API-заглушки
        """
        if tasks_data is None:
            self.tasks_data = [{"id": "api_1", "payload": {
                "action": "send_email", "user": "test@example.com"}},
                {"id": "api_2", "payload": {
                    "action": "calc_stats", "date": "2025-03-08"}},
                {"id": "api_3", "payload": {
                 "action": "log_message", "text": "System started"}},
            ]
        else:
            self.tasks_data = tasks_data

    def get_task(self) -> list[Task]:
        """
        Получение задач из API-заглушки
        
        Returns:
            list[Task]: Список объектов Task
        
        Raises:
            KeyError: Если в данных отсутствуют обязательные поля
        """
        tasks = []

        for task_data in self.tasks_data:
            try:
                task = Task(id=str(task_data['id']),
                            payload=task_data['payload'])
                tasks.append(task)
            except KeyError as e:
                raise KeyError(
                    f"Отсутствует обязательное поле в API-ответе: {e}"
                ) from e
        return tasks
