from django.test import TestCase
from django.urls import reverse
from notes.models import Author, Note

class NoteModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author')
        self.note = Note.objects.create(title='Test Note', content='This is a note.', author=self.author)

    def test_note_str(self):
        self.assertIn('Test Note', str(self.note))
        self.assertIn('Test Author', str(self.note))

    def test_note_has_author(self):
        self.assertEqual(self.note.author.name, 'Test Author')

class NoteViewTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='View Author')
        self.note = Note.objects.create(title='View Note', content='View content', author=self.author)

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Note')
        self.assertContains(response, 'View Author')

    def test_note_detail_view(self):
        response = self.client.get(reverse('note_detail', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View content')

    def test_create_note_via_post(self):
        response = self.client.post(reverse('note_create'), data={
            'title': 'Posted Note',
            'content': 'Posted content',
            'author': self.author.id
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Posted Note')

class AuthorViewTest(TestCase):
    def test_add_author(self):
        response = self.client.post(reverse('author_create'), data={'name': 'New Author'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Author')
