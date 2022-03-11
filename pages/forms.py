from django.forms import ModelForm,widgets
from django import forms
from .models import Page


# Creación del formulario para agregar Proyectos
class PageForm(ModelForm):

    class Meta:
        model = Page
        #fields = ['title', 'description', 'feature_image', 'demo_link','source_link','tags']
        fields = '__all__'
    
    # Sobreescribir el método init para asignarle clases de estilo a los inputs del formulario
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        
        #  Asignar atributos: attrs de forma individual
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': ''})
        self.fields['content'].widget.attrs.update({'class': 'form-control','placeholder': '','rows':'6'})
        self.fields['order'].widget.attrs.update({'class': 'form-control','placeholder': ''})


        # Metodo for para asignar clases a todos los inputs y darles estilo
        # name: clave, field: valor
        """ for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control',}) """
 