from django import forms

class FormularioRegistroPlatos(forms.Form):

    PLATOS=(
        (1, 'Entrada'),
        (2, 'Plato Fuerte'),
        (3, 'Postre'),
        (4, 'Bebidas')
    )

    nombrePlato=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Nombre"
    )

    descripcionPlato=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control mb-3"}),
        max_length=30,
        required=True,
    )

    fotoPlato=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required=True
    )

    precioPlato=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True
    )

    tipoPlato=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-control mb-3"}),
        choices=PLATOS
    )