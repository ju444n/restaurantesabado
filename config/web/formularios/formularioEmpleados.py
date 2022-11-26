from django import forms

class FormularioEmpleados(forms.Form):

    CARGO=(
        (1,'Lava Platos'),
        (2,'Chef'),
        (3,'Mesero')
    )

    nombre=forms.CharField(
        required=True,
        max_length=20,
        label='Nombre del Empleado ',
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    apellido=forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    telefono=forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    direccion=forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    cargo=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-select mb-3'}),
        choices=CARGO
    )