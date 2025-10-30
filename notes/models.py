from django.db import models

class Author(models.Model):
    """Represents a person who owns/creates notes."""
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    """A sticky note with a title, body, author, and timestamp."""
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.author})"
