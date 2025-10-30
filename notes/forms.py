from django import forms
from .models import Note, Author

class AuthorForm(forms.ModelForm):
    """Simple form to add a new author."""
    class Meta:
        model = Author
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Author name'})}

class NoteForm(forms.ModelForm):
    """Form to create/update a note, including selecting an author."""
    class Meta:
        model = Note
        fields = ['title', 'content', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Note title'}),
            'content': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Write your note...'})
        }
