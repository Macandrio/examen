from django import forms
from django.forms import ModelForm
from .models import *
from datetime import *
import re 
from django.utils import timezone
from .forms import *


class CrearPromocioform(ModelForm):
    class Meta:
        model = Promocion  # Asociamos el formulario con el modelo Aeropuerto
        fields='__all__'

        #Como se muestra en el formulario
        labels= {
            "nombre" : ("Nombre  de la Promocion"),
            "descripcion" : ("Descripcion"),
            "descuento" : ("Descuento"),
            "fecha_inicio" : ("Fecha de comienzo"),
            "fecha_fin" : ("Fecha final"),
            "producto" : ("Producto"),
            "usuario" : ("Usuario"),
        }

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Introduce el nombre de la promocion",
                "maxlength": 100,
            }),

            "descripcion": forms.TextInput(attrs={
                "placeholder": "Introduce La Descripcion",
            }),

            "descuento": forms.NumberInput(attrs={
                "placeholder": "Descuento del producto",
            }),

            "fecha_inicio": forms.DateTimeInput(attrs={
                "placeholder": "Introduce la Fecha de incio",
            }),

            "fecha_fin": forms.DateTimeInput(attrs={
                "placeholder": "Introduce la Fecha de final",
            }),

            "nombre": forms.TextInput(attrs={
                "placeholder": "Introduce el nombre de la promocion",
                "maxlength": 100,
            }),

            "esta_activa": forms.CheckboxInput(),



            "producto": forms.Select(),

            "usuario": forms.Select(),
        }

            



    
    def clean(self):
        
        super().clean()
        
        nombre = self.cleaned_data.get('nombre')
        usuario = self.cleaned_data.get('usuario')
        descuento = self.cleaned_data.get('descuento')
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        fecha_fin = self.cleaned_data.get('fecha_fin')
        
        #Comprobamos que no exista un promocion con ese nombre
        encontrar_promocion = Promocion.objects.filter(nombre=nombre).first()
        usuario_edad = Usuario.objects.filter(nombre=nombre).first()

        if(encontrar_promocion):
            self.add_error('nombre','Ya existe una promocion con ese nombre')

        if (descuento > 11 and descuento < 0):
            raise forms.ValidationError("descuento","El descuento no permite ese valor .")
        
        if(fecha_inicio > fecha_fin):
            raise forms.ValidationError("fecha_fin","La fecha final no puede ser inferior a la fecha inicio .")
        
        return self.cleaned_data   
    

class BusquedaAvanzadaPromocion(forms.Form):
    
        nombre = forms.CharField(
            required=False,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contenido...',
            })
        )

        descripcion = forms.CharField(
            required=False,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contenido...',
            })
        )

        descuento = forms.IntegerField(
            required=False,
            widget=forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contenido...',
            })
        )

        fecha_inicio = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Fecha y Hora',
            'type' : 'date'
        })
    )

        fecha_fin = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Fecha y Hora',
            'type' : 'date'
        })
    )


        def clean(self):
            super().clean()

            nombre = self.cleaned_data.get('nombre')
            descripcion = self.cleaned_data.get('descripcion')

            # Validación: Al menos un campo debe estar rellenado
            if not nombre and not descripcion:
                self.add_error('nombre', 'Se debe rellenar minimo un campo')
                self.add_error('descripcion', 'Se debe rellenar minimo un campo')


            return self.cleaned_data
