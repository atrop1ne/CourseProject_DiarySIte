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
    user = User.objects.get(pk = request.user.pk)
    if id == 'add':
        note = Note()
        note.title = ''
        note.description = ''
        note.on_repeat = False
        note.to_remind = False
        note.account = user.account
    else:
        note = Note.objects.get(id = id)

    if request.method == "POST":
        note.title = request.POST.get("title")
        note.description = request.POST.get("description")
        selectedTags = request.POST.getlist("select_tags")
        note.save()
        if selectedTags:
            for st in selectedTags:
                note.tag.add(st)
        note.save()
        return redirect('main')
    else:
        tags = user.account.tags
        return render(request, "DiarySiteApp/noteform.html", {"note": note, 'tags': tags, 'title': 'Ваша заметка'})

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

def addTag(request):
    if request.method == "POST":
        user = User.objects.get(pk = request.user.pk)
        tag = Tag()
        tag.title = request.POST.get("tag_title_input")
        tag.account = user.account
        tag.save()
        return redirect('main')

def deleteTag(request, id):
    tag = Tag.objects.get(id = id)
    tag.delete()
    return redirect('main')

def notesByTag(request, id):
    user = User.objects.get(pk = request.user.pk)
    tags = user.account.tags
    tag = Tag.objects.get(id = id)
    notes = Note.objects.filter(
    account = user.account
    ).filter(
    tag = tag
    )

    photo = user.account.photo
    context ={
        'tags' : tags,
        'notes' : notes,
        'photo' : photo,
        'title' : f'{tag.title}'
    }
    return render(request, 'DiarySiteApp/main.html', context)