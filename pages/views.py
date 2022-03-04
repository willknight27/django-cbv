from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class PageListView(ListView):
    model = Page

    # NOTE: Para que reconzca automaticamente el template sin escribirlo debemos renombrar el html
    # con nombre pages a page_list.html

    # NOTE: El objeto con las paginas que se esta recoreindo en el for se debe renombrar a object_list o page_list


class PageDetailView(DetailView):
    model = Page

    # NOTE: Para que reconzca automaticamente el template sin escribirlo debemos renombrar el html
    # con nombre pages a page_detail.html
