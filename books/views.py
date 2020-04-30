from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book
from .forms import ReviewForm
from django.urls import reverse



class books_list_view(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books_list.html'
    login_url = 'account_login'


class books_detail_view(LoginRequiredMixin,DetailView):
    form = ReviewForm()
    model = Book
    context_object_name = 'book'
    template_name = 'books_detail.html'
    login_url = 'account_login'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self,request, *args, **kwargs):
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            book = self.get_object()
            form.instance.author = request.user
            form.instance.book = book
            form.save()
            return redirect(
                reverse('books_detail', args=[str(book.pk)])
            )