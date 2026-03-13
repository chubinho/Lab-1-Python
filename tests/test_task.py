from src.task import Task


class TestTask:

    def test_task_attributes(self):
        """Проверка создания задачи"""
        task = Task(id='12345', payload={"test": "the best"})
        assert task.id == '12345'
        assert task.payload == {"test": "the best"}

    def test_task_with_complex_payload(self):
        """Проверка задачи со сложным payload"""
        payload = {
            "dict": {"key": "value"},
            "list": [1, 2, 3, 5, 151, 51],
            "bool": True
        }
        task = Task(id="complex", payload=payload)

        assert len(task.payload["list"]) == 6
        assert task.payload['list'][0] == 1
        assert task.id == "complex"
        assert task.payload["dict"]["key"] == "value"
        
    def test_task_empty_payload(self):
        """Проверка задачи с пустым payload"""
        task = Task(id="empty", payload={})
        assert task.id == "empty"
        assert task.payload == {}
