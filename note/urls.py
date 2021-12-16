from django.urls import path
from note.views import (NoteCreateView, NoteDeleteView, NoteDetailView,
    NoteListView, NoteUpdateView, AuthorNoteList)
app_name = 'note'

urlpatterns = [
    #path('', name='home'),
    path('<str:username>/create/', NoteCreateView.as_view(), name='note-create-form'),
    path('delete/<str:username>/<slug:slug>', NoteDeleteView.as_view(), name='note-delete'),
    path('detail/<slug:slug>', NoteDetailView.as_view(), name='note-detail'),
    path('list/', NoteListView.as_view(), name='note-list'),
    path('update/<slug:slug>', NoteUpdateView.as_view(), name='note-update'),
    path('author/list/', AuthorNoteList.as_view(), name='author-note-list')
]
