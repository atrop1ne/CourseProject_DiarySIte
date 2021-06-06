from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import *
import datetime
from django.forms.models import model_to_dict

def index(request):
    return render(request, 'DiarySiteApp/index.html', {'title' : 'DiaryLight'})

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
    response = redirect('trashCan')
    count = 0
    if 'inTrashCan' in request.COOKIES:
        count = request.COOKIES['inTrashCan']
        count = int(count) - 1
    response.set_cookie('inTrashCan', count)
    return response

def toTrashCanNote(request, id):
    note = Note.objects.get(id=id)
    note.on_delete = True
    note.delete_date = datetime.datetime.now().date()
    note.save()
    response = redirect('main')
    count = 1
    if 'inTrashCan' in request.COOKIES:
        count = request.COOKIES['inTrashCan']
        count = int(count) + 1
    response.set_cookie('inTrashCan', count)
    return response


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
    response = redirect('trashCan')
    response.set_cookie('inTrashCan', 0)
    return response

def addTag(request):
    if request.method == "POST":
        user = User.objects.get(pk = request.user.pk)
        tag = Tag()
        tag.title = request.POST.get("tag_title_input")
        tag.account = user.account
        tag.save()
        return JsonResponse({'tag': model_to_dict(tag)}, status = 200)

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