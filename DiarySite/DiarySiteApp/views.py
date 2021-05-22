from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import *
import datetime

def index(request):
    return render(request, 'DiarySiteApp/index.html', {'title' : 'Diary Site'})

def main(request):
    user = User.objects.get(pk = request.user.pk)
    tags = user.account.tags
    notes = Note.objects.filter(
    account = user.account
    ).filter(
    on_delete = False
    )

    photo = user.account.photo
    context ={
        'tags' : tags,
        'notes' : notes,
        'photo' : photo,
        'title' : 'Главная страница'
    }
    return render(request, 'DiarySiteApp/main.html', context)

def noteView(request, id):
    if id == 'add':
        note = Note()
        note.title = ''
        note.description = ''
        note.on_repeat = False
        note.to_remind = False
        user = User.objects.get(pk = request.user.pk)
        note.account = user.account
    else:
        note = Note.objects.get(id = id)

    if request.method == "POST":
        note.title = request.POST.get("title")
        note.description = request.POST.get("description")
        note.save()
        return redirect('main')
    else:
        return render(request, "DiarySiteApp/noteform.html", {"note": note, 'title': 'Ваша заметка'})

def restoreNote(request, id):
    note = Note.objects.get(id=id)
    note.on_delete = False
    note.save()
    return redirect('trashCan')

def toTrashCanNote(request, id):
    note = Note.objects.get(id=id)
    note.on_delete = True
    note.delete_date = datetime.datetime.now().date()
    note.save()
    return redirect('main')

def trashCanView(request):
    user = User.objects.get(pk = request.user.pk)
    tags = user.account.tags
    notes = Note.objects.filter(
    account = user.account
    ).filter(
    on_delete = True
    )

    photo = user.account.photo
    context ={
        'tags' : tags,
        'notes' : notes,
        'photo' : photo,
        'title' : 'Корзина'
    }
    return render(request, 'DiarySiteApp/trashCan.html', context)

def deleteNote(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('trashCan')

def clearTrashCan(request):
    user = User.objects.get(pk = request.user.pk)
    notes = Note.objects.filter(
    account = user.account
    ).filter(
    on_delete = True
    )
    notes.delete()
    return redirect('trashCan')