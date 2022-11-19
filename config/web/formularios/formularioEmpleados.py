from django import forms

class FormularioRegistroEmpleados(forms.Form):

    EMPLEADOS=(
        (1, 'Gerente'),
        (2, 'Chef'),
        (3, 'Mesero'),
        (4, 'Cajero')
    )

    nombreEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Nombre"
    )

    apellidoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=30,
        required=True,
    )

    fotoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required=True
    )

    documentoEmpleado=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True
    )

    tipoEmpleado=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-control mb-3"}),
        choices=EMPLEADOS
    )