from django.urls import path
from django.urls.conf import re_path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    re_path(r'^main', views.main, name = 'main'),
    re_path(r'^noteform/(?P<id>\w+)$', views.noteView, name = 'noteform'),
    re_path(r'^toTrashCan/(?P<id>\d+)$', views.toTrashCanNote, name = 'toTrashCan'),
    re_path('trashCan', views.trashCanView, name = 'trashCan'),
    path('clearTrashCan', views.clearTrashCan, name = 'clearTrashCan'),
    re_path(r'^delete/(?P<id>\d+)$', views.deleteNote, name = 'delete'),
    re_path(r'^restoreNote/(?P<id>\d+)$', views.restoreNote, name = 'restoreNote'),
    path('addTag', views.addTag, name='addTag'),
    re_path(r'^deleteTag/(?P<id>\d+)$', views.deleteTag, name = 'deleteTag'),
    re_path(r'^notesByTag/(?P<id>\d+)$', views.notesByTag, name = 'notesByTag'),
]