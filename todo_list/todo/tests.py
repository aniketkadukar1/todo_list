from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    def test_task_model_exis(self):
        tasks = Task.objects.count()
        self.assertEqual(tasks, 0)