from django.shortcuts import render, get_object_or_404
from .forms import NoteForm
from .models import Note
from .utils import generate_jwt, decode_jwt
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.conf import settings

def landing_page(request):
    return render(request, "landing_page.html")

def how_to_use(request):
    return render(request, "how_to_use.html")

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            token = generate_jwt(note.id)
            qr = qrcode.make(f"{settings.QR_BASE_URL}/notes/view/{token}/")
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            img_data = buffer.getvalue()
            return render(request, 'note_created.html', {'note': note, 'qr_image': img_data})
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})

def view_note(request, token):
    try:
        payload = decode_jwt(token)
        note = get_object_or_404(Note, id=payload['note_id'])
        return render(request, 'view_note.html', {'note': note})
    except:
        return render(request, 'invalid_note.html')

def about(request):
    return render(request, "about.html")
