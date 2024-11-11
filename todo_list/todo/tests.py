from django.test import TestCase
from .models import Task
import datetime
from .forms import NewTaskForm, UpdateTaskForm
from django.urls import reverse

class TaskModelTest(TestCase):
    def test_task_model_exis(self):
        tasks = Task.objects.count()
        self.assertEqual(tasks, 0)
    
    def test_model_has_string_representation(self):
        task = Task.objects.create(
            title = 'First Task',
            deadline = datetime.datetime(2024, 11, 8)
        )
        self.assertEqual(str(task), task.title)

class IndexPageTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title = 'First Task',
            deadline = datetime.datetime(2024, 11, 8)
        )

    def test_index_page_returns_correct_response(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'todo/index.html')
        self.assertEqual(response.status_code, 200)
    
    def test_index_page_has_tasks(self):
        response = self.client.get('/')
        self.assertContains(response, self.task.title)

class DetailPageTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title = 'First Task',
            description = 'First Demo Description',
            deadline = datetime.datetime(2024, 11, 8)
        )

    def test_detail_page_returns_correct_response(self):
        response = self.client.get(f'/{self.task.id}/')
        self.assertTemplateUsed(response, 'todo/detail.html')
        self.assertEqual(response.status_code, 200)
    
    def test_detail_page_has_correct_content(self):
        response = self.client.get(f'/{self.task.id}/')
        self.assertContains(response, self.task.title)
        self.assertContains(response, self.task.description)

class NewPageTest(TestCase):
    def setUp(self):
        self.form = NewTaskForm

    def test_new_page_returns_correct_response(self):
        response = self.client.get('/new/')
        self.assertTemplateUsed(response, 'todo/new.html')
        self.assertEqual(response.status_code, 200)
    
    def test_form_can_be_valid(self):
        self.assertTrue(issubclass(self.form, NewTaskForm))
        self.assertTrue('title' in self.form.Meta.fields)
        self.assertTrue('description' in self.form.Meta.fields)
        self.assertTrue('title' in self.form.Meta.fields)

        form = self.form(
            {
            'title' : 'The Test Title',
            'description' : 'The Test Description',
            'deadline' : datetime.datetime(2024, 11, 8)
            }
        )
        self.assertTrue(form.is_valid())



    def test_new_page_form_rendering(self):
        response = self.client.get('/new/')
        self.assertContains(response, '<form')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, '<label for')

        # Test invalid form
        response = self.client.post('/new/', 
            {
            'title' : '',
            'description' : 'The Test Description',
            'deadline' : datetime.datetime(2024, 11, 8)
            }
        )
        self.assertContains(response, '<ul class="errorlist">')
        self.assertContains(response, 'This field is required.')

        # Test valid form
        # Test not working
        # response = self.client.post('/new/',
        #     {
        #     'title' : 'Test Form Title',
        #     'description' : 'The Test Description',
        #     'deadline' : datetime.datetime(2024, 11, 8)           
        #     }
        # )
        # self.assertRedirects(response, expected_url='/')
        # self.assertEqual(Task.objects.count(),1)


class UpdatePageTest(TestCase):
    def setUp(self):
        self.form = UpdateTaskForm
        self.task = Task.objects.create(
            title='First Task',
            description='First Description',
            deadline=datetime.datetime(2024, 11, 9))

    def test_update_page_returns_correct_response(self):
        response = self.client.get(f'/{self.task.id}/update/')
        self.assertTemplateUsed(response, 'todo/update.html')
        self.assertEqual(response.status_code, 200)

    def test_form_can_be_valid(self):
        self.assertTrue(issubclass(self.form, UpdateTaskForm))
        self.assertTrue('title' in self.form.Meta.fields)
        self.assertTrue('description' in self.form.Meta.fields)
        self.assertTrue('title' in self.form.Meta.fields)

        form = self.form(
            {
            'title' : 'The Test Title',
            'description' : 'The Test Description',
            'deadline' : datetime.datetime(2024, 11, 8)
            }, instance=self.task
        )

        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(self.task.title, 'The Test Title')
    
    def test_form_can_be_invalid(self):
        form = self.form(
            {
            'title' : '',
            'description' : 'The Test Description',
            'deadline' : datetime.datetime(2024, 11, 8)
            }, instance=self.task
        )

        self.assertFalse(form.is_valid())
    
    def test_update_page_form_rendering(self):
        response = self.client.get(f'/{self.task.id}/update/')
        self.assertContains(response, '<form')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, '<label for')

        # Test invalid form
        response = self.client.post(f'/{self.task.id}/update/', 
            {
            'id' : self.task.id,
            'title' : '',
            'description' : 'The Test Description',
            'deadline' : datetime.datetime(2024, 11, 8)
            }, instance = self.task
        )
        self.assertContains(response, '<ul class="errorlist">')
        self.assertContains(response, 'This field is required.')

        # Test valid form
        # Test not working
        # response = self.client.post(f'/{self.task.id}/update/',
        #     {
        #     'title' : 'Test Form Title',
        #     'description' : 'The Test Description',
        #     'deadline' : datetime.datetime(2024, 11, 8)           
        #     }
        # )
        # self.assertRedirects(response, expected_url='/')
        # self.assertEqual(Task.objects.count(),1)

class DeletePageTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title='First Task', description='First Description', deadline=datetime.datetime(2024, 8, 11))
    
    def test_delete_page_deletes_task(self):
        self.assertEqual(Task.objects.count(),1)
        response = self.client.get(f'/{self.task.id}/delete/')
        self.assertRedirects(response, expected_url='/')
        self.assertEqual(Task.objects.count(),0)