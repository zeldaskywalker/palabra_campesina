from django.views import generic
from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .access_form import AccessForm
from .access_form import AccesoForm

from . import baserow


def contraseña_or_password_view(request):

    language = request.session.get('language', 'es')

    # check to see if session already has a successful site password saved
    # if so, redirect to inicio
    session_password_saved = request.session.get('site_password')
    if session_password_saved:
        if session_password_saved == 'en':
            return redirect('home')
        else:
            return redirect('inicio')
    
    # otherwise, get password within submitted form
    if request.method == 'POST':
        if 'password' in request.POST:
            password = request.POST.get('password')

            # if the password in the form matches the expected site password...
            if (password == settings.SITE_PASSWORD):
                # save the successful site password to session,
                request.session['site_password'] = password
                if language == 'en':
                    return redirect('home')
                else:
                    # and redirect to inicio
                    return redirect('inicio')
            else:
                # otherwise, state that the password is incorrect and to try again
                messages.error(request, 'Incorrect password. Please try again.')

        if 'language_change' in request.POST:
            new_language = request.POST.get('language')
            request.session['language'] = new_language

    return render(request, 'contraseña.html')

# Español
class InicioView(generic.TemplateView):
    template_name = 'español/inicio.html'

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'es'

        context = super().get_context_data(**kwargs)
        context['title'] = 'INICIO'
        context['redirect'] = '/home'
        return context

class GaleriaOverallView(generic.ListView):
    template_name = 'español/galeria.html'
    data = baserow.get_gallery_all_images()

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'es'

        context = super(GaleriaOverallView, self).get_context_data(**kwargs)
        context['title'] = 'GALERÍA'
        context['redirect'] = '/gallery'
        context['data'] = self.data

        api_image_urls = []
        for row in self.data:
            api_image_urls.append(row['image'][0]['url'])

        context['api_image_urls'] = api_image_urls
        return context

    def get_queryset(self, **kwargs):
        return self.data

class GaleriaImageView(generic.TemplateView):
    template_name = 'español/galeria_image.html'

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'es'

        context = super(GaleriaImageView, self).get_context_data(**kwargs)
        context['redirect'] = '/gallery/' + str(context['row_id'])
        context['data'] = baserow.get_gallery_image_singular(context['row_id'])
        context['title'] = context['data']['title']

        api_image_url = context['data']['image'][0]['url']
        context['api_image_urls'] = [api_image_url]
        return context

class TestimoniosView(generic.ListView):
    template_name = 'español/testimonios.html'
    data = baserow.get_testimonios_all()

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'es'

        context = super(TestimoniosView, self).get_context_data(**kwargs)
        context['redirect'] = '/testimonies'
        context['data'] = self.data
        context['title'] = 'TESTIMONIOS'
        return context

    def get_queryset(self, **kwargs):
        return self.data
    
class TestimonioView(generic.TemplateView):
    template_name = 'español/testimonio.html'

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'es'

        context = super(TestimonioView, self).get_context_data(**kwargs)
        context['redirect'] = '/testimony/' + str(context['row_id'])
        context['data'] = baserow.get_testimonio(context['row_id'])
        context['title'] = context['data']['title']
        return context
 
class SobreView(generic.TemplateView):
    template_name = 'español/sobre.html'

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'es'

        context = super().get_context_data(**kwargs)
        context['redirect'] = '/about'
        context['title'] = 'SOBRE'
        return context

class GraciasView(generic.TemplateView):
    template_name = 'español/gracias.html'

class AccesoView(generic.FormView):
    form_class = AccesoForm
    template_name = 'español/acceso.html'

    def get_success_url(self):
        return reverse("gracias")

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'es'

        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        nombre = form.cleaned_data.get("nombre")
        correo_electrónico = form.cleaned_data.get("correo_electrónico")
        organización_o_afiliación = form.cleaned_data.get("organización_o_afiliación")
        mensaje = form.cleaned_data.get("mensaje")

        html_content = render_to_string('email.html',
                                        {'name': nombre,
                                         'email': correo_electrónico,
                                         'org_or_affiliation': organización_o_afiliación,
                                         'message': mensaje})

        full_message = f"""
            The following details were provided with this request:
            ________________________


            NAME:
            {nombre}

            EMAIL ADDRESS:
            {correo_electrónico}

            ORGANIZATION OR AFFILIATION:
            {correo_electrónico}

            Why are you requesting access?:
            {mensaje}
            """
        send_mail(
            subject="Access Requested to Palabra Campesina",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            html_message=html_content
        )
        return super().form_valid(form)

# English
class HomeView(generic.TemplateView):
    template_name = 'english/home.html'

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'en'

        context = super().get_context_data(**kwargs)
        context['title'] = 'HOME'
        context['redirect'] = '/inicio'
        return context

class GalleryOverallView(generic.ListView):
    template_name = 'english/gallery.html'
    data = baserow.get_gallery_all_images()

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'en'

        context = super(GalleryOverallView, self).get_context_data(**kwargs)
        context['redirect'] = '/galeria'
        context['data'] = self.data
        context['title'] = 'GALLERY'

        api_image_urls = []
        for row in self.data:
            api_image_urls.append(row['image'][0]['url'])

        context['api_image_urls'] = api_image_urls
        return context

    def get_queryset(self, **kwargs):
        return self.data

class GalleryImageView(generic.TemplateView):
    template_name = 'english/gallery_image.html'

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'en'

        context = super(GalleryImageView, self).get_context_data(**kwargs)
        context['redirect'] = '/galeria/' + str(context['row_id'])
        context['data'] = baserow.get_gallery_image_singular(context['row_id'])
        context['title'] = context['data']['title']

        api_image_url = context['data']['image'][0]['url']
        context['api_image_urls'] = [api_image_url]
        return context

class TestimoniesView(generic.ListView):
    template_name = 'english/testimonies.html'
    data = baserow.get_testimonios_all()

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'en'

        context = super(TestimoniesView, self).get_context_data(**kwargs)
        context['redirect'] = '/testimonios'
        context['data'] = self.data
        context['title'] = 'TESTIMONIES'
        return context

    def get_queryset(self, **kwargs):
        return self.data
    
class TestimonyView(generic.TemplateView):
    template_name = 'english/testimony.html'

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'en'

        context = super(TestimonyView, self).get_context_data(**kwargs)
        context['redirect'] = '/testimonio/' + str(context['row_id'])
        context['data'] = baserow.get_testimonio(context['row_id'])
        context['title'] = context['data']['title']
        return context
 
class AboutView(generic.TemplateView):
    template_name = 'english/about.html'

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'en'

        context = super().get_context_data(**kwargs)
        context['redirect'] = '/sobre'
        context['title'] = 'ABOUT'
        return context

class ThanksView(generic.TemplateView):
    template_name = 'english/thanks.html'

class AccessView(generic.FormView):
    form_class = AccessForm
    template_name = 'english/access.html'

    def get_success_url(self):
        return reverse("thanks")

    def get_context_data(self, **kwargs):
        self.request.session['language'] = 'en'

        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        name = form.cleaned_data.get("name")
        organization_or_affiliation = form.cleaned_data.get("organization_or_affiliation")
        message = form.cleaned_data.get("message")

        html_content = render_to_string('email.html',
                                        {'name': name,
                                         'email': email,
                                         'org_or_affilitaion': organization_or_affiliation,
                                         'message': message})

        full_message = f"""
            The following details were provided with this request:
            ________________________


            NAME:
            {name}

            EMAIL ADDRESS:
            {email}

            ORGANIZATION OR AFFILIATION:
            {organization_or_affiliation}

            Why are you requesting access?:
            {message}
            """
        send_mail(
            subject="Access Requested to Palabra Campesina",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            html_message=html_content
        )
        return super().form_valid(form)
