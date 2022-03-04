from django.urls import path
from .views import home,sample

urlpatterns = [
    path('', home, name="home"),
    path('sample/', sample, name="sample"),
]