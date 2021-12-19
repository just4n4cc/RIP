from django import forms
from django.shortcuts import render
from .models import Library, Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    return render(request, 'index.html')


def report(request):
    books = Book.objects.report()
    return render(request, 'report.html', {'books': books})


def book_list(request):
    books = Book.objects.ordered()
    return render(request, 'list.html', {'objs': books, 'name': 'Books'})


def lib_list(request):
    libs = Library.objects.ordered()
    return render(request, 'list.html', {'objs': libs, 'name': 'Libraries'})


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'pub_year', 'lib_id']
    success_url = '/book'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super(BookCreate, self).get_context_data(**kwargs)
        context['name'] = 'Create'
        context['entity'] = 'book'
        context['form'].fields['lib_id'] = forms.ModelChoiceField(queryset=Library.objects.all(),
                                                                  empty_label=None, label='Library')
        return context


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'pub_year', 'lib_id']
    success_url = '/book'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super(BookUpdate, self).get_context_data(**kwargs)
        context['name'] = 'Update'
        context['entity'] = 'book'
        context['form'].fields['lib_id'] = forms.ModelChoiceField(queryset=Library.objects.all(),
                                                                  empty_label=None, label='Library')
        return context


class BookDelete(DeleteView):
    model = Book
    pk_url_kwarg = 'book_id'
    success_url = '/book'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super(BookDelete, self).get_context_data(**kwargs)
        context['name'] = 'Delete'
        context['entity'] = 'book'
        context['delete'] = True
        return context


class LibCreate(CreateView):
    model = Library
    fields = ['name', 'phone', 'email']
    success_url = '/library'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super(LibCreate, self).get_context_data(**kwargs)
        context['name'] = 'Create'
        context['entity'] = 'library'
        return context


class LibUpdate(UpdateView):
    model = Library
    fields = ['name', 'phone', 'email']
    success_url = '/library'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super(LibUpdate, self).get_context_data(**kwargs)
        context['name'] = 'Update'
        context['entity'] = 'library'
        return context


class LibDelete(DeleteView):
    model = Library
    pk_url_kwarg = 'lib_id'
    success_url = '/library'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super(LibDelete, self).get_context_data(**kwargs)
        context['name'] = 'Delete'
        context['entity'] = 'library'
        context['delete'] = True
        return context

