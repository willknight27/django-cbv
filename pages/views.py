from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from pages.forms import PageForm
from django.urls import reverse, reverse_lazy


class PageListView(ListView):
    model = Page

    # NOTE: Para que reconzca automaticamente el template sin escribirlo debemos renombrar el html
    # con nombre pages a page_list.html

    # NOTE: El objeto con las paginas que se esta recoreindo en el for se debe renombrar a object_list o page_list


class PageDetailView(DetailView):
    model = Page

    # NOTE: Para que reconzca automaticamente el template sin escribirlo debemos renombrar el html
    # con nombre pages a page_detail.html


class PageCreateView(CreateView):

    model = Page
    form_class= PageForm
    # Redirecion a la pagina si el formulario es correcto
    success_url = reverse_lazy('pages:pages')