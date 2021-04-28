from django.views.generic.edit import CreateView
from django.shortcuts import render

def index(request):
    return render(request, 'DiarySiteApp/index.html')

def main(request):
    return render(request, 'DiarySiteApp/main.html')