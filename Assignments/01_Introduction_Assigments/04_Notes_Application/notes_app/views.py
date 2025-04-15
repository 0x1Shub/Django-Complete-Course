from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Category
from .forms import NoteForm

def note_list(request):
    categories = Category.objects.all()
    notes_by_category = {}

    for category in categories:
        notes_by_category[category] = Note.objects.filter(category=category)

    return render(request, 'notes_app/note_list.html', {'notes_by_category': notes_by_category})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes_app/note_form.html', {'form': form})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes_app/note_form.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
