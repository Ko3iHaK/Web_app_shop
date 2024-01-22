from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from django.contrib.auth.models import User
from .models import Article, Cart


def books_home(request):
   bd = Article.objects.all()
   return render(request, 'bd/books_home.html', {'bd' : bd, 'title' : 'Книги'})

def show_book(request, book_id):
    book = get_object_or_404(Article, pk=book_id)

    data = {
     'book' : book,
     'title' : book.title,

    }
    return render(request, 'bd/book.html', context=data)





class books_home(ListView):
    paginate_by = 4
    model = Article
    template_name = 'bd/books_home.html'
    context_object_name = 'books'
    #session_key = request.session.session_key
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Книги'
        return  context




class CartUser(ListView):
    paginate_by = 4
    model = Cart

    template_name = 'bd/cart.html'
    context_object_name = 'cart'

    def get_context_data(self, *, object_list=None, **kwargs):
        bd = User.objects.all()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Корзина'
        context['user'] = bd
        return  context


