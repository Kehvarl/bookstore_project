from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Book


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     DetailView):
    model = Book
    comtext_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class SearchResultsListView(ListView):
    """
    View for search results
    with filtering based on title
    """
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        return Book.objects.filter(
            Q(title__icontains='beginners') | Q(title__icontains='test')
        )
