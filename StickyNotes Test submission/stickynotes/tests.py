"""Unit tests for the Sticky Notes app."""

from django.test import TestCase
from django.urls import reverse, NoReverseMatch
from .models import Note


def url_or(path_name, fallback, *args):
    """
    Safely resolve a URL name or use a fallback path.

    Args:
        path_name (str): The named URL pattern.
        fallback (str): A fallback path if reversing fails.
        *args: Optional positional arguments for reverse().

    Returns:
        str: The resolved or fallback URL.
    """
    try:
        return reverse(path_name, args=args) if args else reverse(path_name)
    except NoReverseMatch:
        return fallback


class NoteModelTest(TestCase):
    """Tests for the Note model."""

    def test_create_note_minimal(self):
        """Test creating a simple note and verifying its fields."""
        note = Note.objects.create(title="Test", content="Hello")
        self.assertIsNotNone(note.pk)
        self.assertEqual(note.title, "Test")
        self.assertEqual(note.content, "Hello")


class NoteViewsTest(TestCase):
    """Tests for Sticky Notes views and CRUD flows."""

    def setUp(self):
        """Create a default note to use in view tests."""
        self.note = Note.objects.create(title="First", content="Body")

    def test_home_page_loads(self):
        """Home page should load and display the first note."""
        home_url = url_or("home", "/")
        response = self.client.get(home_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First")

    def test_add_note_flow(self):
        """Test that a new note can be added successfully."""
        add_url = url_or("add_note", "/add/")
        response = self.client.post(
            add_url,
            {"title": "New", "content": "Something"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New")

    def test_edit_note_flow(self):
        """Test editing an existing note updates its content."""
        edit_url = url_or("edit_note", f"/edit/{self.note.id}/", self.note.id)
        response = self.client.post(
            edit_url,
            {"title": "Updated", "content": "Changed"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Updated")

    def test_delete_note_flow(self):
        """Test deleting a note removes it from the page."""
        delete_url = url_or("delete_note", f"/delete/{self.note.id}/", self.note.id)
        response = self.client.post(delete_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "First")
