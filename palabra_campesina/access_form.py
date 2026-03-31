from django import forms


class AccessForm(forms.Form):
    name = forms.CharField(
        label="Name (required):",
        widget=forms.TextInput(attrs={"style": "width:100%;"})
    )

    email = forms.EmailField(
        label="Email Address (required):",
        widget=forms.TextInput(attrs={"style": "width:100%;"})
    )

    organization_or_affiliation = forms.CharField(
        required=False, # optional
        label="Organization or Affiliation (optional):",
        widget=forms.TextInput(attrs={"style": "width:100%;"})
    )
    message = forms.CharField(
        label="Why are you requesting access? (required):",
        widget=forms.Textarea(attrs={"placeholder": "Please briefly describe how you intend to use this resource.", "style": "width:100%; height: 10vh;"})
    )

class AccesoForm(forms.Form):
    nombre = forms.CharField(
        label="Tu Nombre (requerido):",
        widget=forms.TextInput(attrs={"style": "width:100%;"})
    )

    correo_electrónico = forms.EmailField(
        label="Correo Electrónico (requerido):",
        widget=forms.TextInput(attrs={"style": "width:100%;"})
    )

    organización_o_afiliación = forms.CharField(
        label="Organización o Afiliación (opcional):",
        required=False, # optional
        widget=forms.TextInput(attrs={"placeholder": "Opcional", "style": "width:100%;"})
    )

    mensaje = forms.CharField(
        label="¿Por qué estás solicitando acceso? (requerido):",
        widget=forms.Textarea(attrs={"placeholder": "Please briefly describe how you intend to use this resource.", "style": "width:100%; height: 10vh;"})
    )
