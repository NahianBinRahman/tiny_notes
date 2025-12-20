from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Note

def index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})

@require_http_methods(["POST"])
def add_note(request):
    content = request.POST.get('content')
    if content:
        note = Note.objects.create(content=content)
        return render(request, 'notes/partials/note.html', {'note': note})
    return HttpResponse("")

@require_http_methods(["POST"])
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    content = request.POST.get('content')
    if content:
        note.content = content
        note.save()
    return render(request, 'notes/partials/note.html', {'note': note})

@require_http_methods(["DELETE"])
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return HttpResponse("")
