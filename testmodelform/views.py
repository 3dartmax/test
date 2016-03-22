from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Author, Book
from .forms import AuthorForm, BookForm

author_list   = ListView.as_view(model=Author)
author_detail = DetailView.as_view(model=Author)
author_new    = CreateView.as_view(model=Author, form_class=AuthorForm, template_name='testmodelform/author_form.html')

book_list     = ListView.as_view(model=Book)
book_detail   = DetailView.as_view(model=Book)
book_new      = CreateView.as_view(model=Book, form_class=BookForm, template_name='testmodelform/book_form.html')
