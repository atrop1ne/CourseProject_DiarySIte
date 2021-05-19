from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'DiarySiteApp/index.html', {'title' : 'Diary Site'})

def main(request):
    user = User.objects.get(pk = request.user.pk)
    tags = user.account.tags
    notes = user.account.notes
    photo = user.account.photo
    context ={
        'tags' : tags,
        'notes' : notes,
        'photo' : photo,
        'title' : 'Главная страница'
    }
    return render(request, 'DiarySiteApp/main.html', context)