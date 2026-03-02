from django.views import generic
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

from . import baserow

def site_password_view(request):
    # check to see if session already has a successful site password saved
    # if so, redirect to inicio
    session_password_saved = request.session.get('site_password')
    if session_password_saved:
        print('session already saved password')
        print(session_password_saved)
        return redirect('inicio')
    
    # otherwise, get password within submitted form
    if request.method == 'POST':
        password = request.POST.get('password')

        # if the password in the form matches the expected site password...
        if (password == settings.SITE_PASSWORD):
            # save the successful site password to session,
            request.session['site_password'] = password
            # and redirect to inicio
            return redirect('inicio')
        else:
            # otherwise, state that the password is incorrect and to try again
            messages.error(request, "Incorrect password. Please try again.")

    return render(request, 'password.html')

class InicioView(generic.TemplateView):
    template_name = 'inicio.html'

class GaleriaOverallView(generic.ListView):
    template_name = 'galeria.html'
    data = baserow.get_gallery_all_images()

    def get_context_data(self, **kwargs):
        context = super(GaleriaOverallView, self).get_context_data(**kwargs)
        context['data'] = self.data
        return context

    def get_queryset(self, **kwargs):
        return self.data

class GaleriaImageView(generic.TemplateView):
    template_name = 'galeria_image.html'

    def get_context_data(self, **kwargs):
        context = super(GaleriaImageView, self).get_context_data(**kwargs)
        context['data'] = baserow.get_gallery_image_singular(context['row_id'])
        return context['data']
  
class TestimoniosView(generic.ListView):
    template_name = 'testimonios.html'
    data = baserow.get_stories_all()

    def get_context_data(self, **kwargs):
        context = super(TestimoniosView, self).get_context_data(**kwargs)
        context['data'] = self.data
        return context

    def get_queryset(self, **kwargs):
        return self.data

# class StoryView(generic.TemplateView):
#     template_name = 'palabra.html'

#     def get_context_data(self, **kwargs):
#         context = super(StoryView, self).get_context_data(**kwargs)
#         context['data'] = baserow.get_story(context['row_id'])
#         return context['data']
 
class SobreView(generic.TemplateView):
    template_name = 'sobre.html'