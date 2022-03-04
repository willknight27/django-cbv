from django.views.generic.base import TemplateView # Para renderizar un template
from django.shortcuts import render


class HomePageView(TemplateView):

    template_name = 'core/home.html'

    """ def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Asignar un aclve y valor al diccionario del contexto
        #context['titulo'] = 'Mensaje de ejemplo desde el contexto (CBV)'

        context = {
            'title': 'Titulo de ejemplo desde la vista basada en clase'
        }

        return context """
    
    # Otra forma mas simple de retornar un contexto con render
    # Procesar la respuesta de la vista definida en el metodo get
    def get(self,request, *args, **kwargs):

        context = {
            'title': 'Título de ejemplo desde la vista basada en clase'
        }

        return render(request, self.template_name,context)
    

class SamplePageView(TemplateView):
    template_name = 'core/sample.html'
