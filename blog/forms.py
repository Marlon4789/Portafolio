from django import forms
from .models import QuillPost
class QuillPostForm(forms.ModelForm):

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content.strip():
            raise forms.ValidationError('El contenido no puede estar vacio')
        return content

    class Meta:
        model = QuillPost
        fields = ('title', 'image_url', 'description', 'content',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la URL de la imagen'}),
        }
        labels = {
            'title': 'Crear titulo',
            'description': 'Descripción',
            'content': '',
            'image_url': 'Subir imagen',
        }

