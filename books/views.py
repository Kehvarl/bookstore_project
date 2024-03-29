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
    Load Search Results and Display Them
    Request -> GET -> q:   terms to search in title and author.
    """
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None:
            return Book.objects.all()
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
