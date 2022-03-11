from django.urls import path
from .views import PageListView, PageDetailView,PageCreateView

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    # cambiar  <int:page_id> por <int:pk> para que la vista basada en clase reconozca el parametro del id en la url
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name='create'),

], 'pages')