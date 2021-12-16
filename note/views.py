from django.shortcuts import render, get_object_or_404
from note.models import Note
from accounts.models import CustomUser
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#Create your views here.

class NoteListView(ListView):
    model = Note
    template_name = 'note_list'
    context_object_name = 'notes'


class AuthorNoteList(ListView):
    """
    List for currently logged in user
    """
    #try/ why make it a detail view
    #how change functionality to show detail list by author and implement for
    #currently logged in user
    template_name = 'note/author_note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        self.author = get_object_or_404(CustomUser, username=self.request.user)
        return Note.objects.filter(author=self.author)



class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/note_detail.html'
    context_object_name = 'note'

    """def get(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)"""


class NoteCreateView(LoginRequiredMixin, CreateView):
    login_url = 'accounts:login'
    model = Note
    fields = ['title', 'body', 'status']
    template_name_suffix = '_create_form'



class NoteOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        note = self.get_object()
        if self.request.user in note.author.all():
            return True
        return False



class NoteUpdateView(LoginRequiredMixin, NoteOwnerMixin, UpdateView):
    login_url = 'accounts:login'
    model = Note
    fields = ['title', 'body', 'status']
    template_name_suffix = '_update_form'


class NoteDeleteView(LoginRequiredMixin, NoteOwnerMixin, DeleteView):
    login_url = 'accounts:login'
    model = Note
    success_url = reverse_lazy('note:note-list')
    template_name_suffix = '_check_delete'