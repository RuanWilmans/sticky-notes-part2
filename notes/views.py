from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Author
from .forms import NoteForm, AuthorForm

# ---------- Notes ----------

def note_list(request):
    """List all notes, newest first."""
    notes = Note.objects.select_related('author').all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes, 'page_title': 'Sticky Notes'})

def note_detail(request, pk):
    """View a single note."""
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_create(request):
    """Create a new note."""
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def note_update(request, pk):
    """Edit an existing note."""
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'note': note})

def note_delete(request, pk):
    """Delete a note after confirmation POST."""
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_detail.html', {'note': note})

# ---------- Authors ----------

def author_list(request):
    """List all authors and the number of notes they have."""
    authors = Author.objects.all().order_by('name')
    return render(request, 'notes/author_list.html', {'authors': authors})

def author_create(request):
    """Add a new author (requested in Part 2 review)."""
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'notes/author_form.html', {'form': form})
