from django.views import generic
from django.shortcuts import render
from . import baserow

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
    
class HistoriasView(generic.ListView):
    template_name = 'historias.html'
    data = baserow.get_stories_all()

    def get_context_data(self, **kwargs):
        context = super(HistoriasView, self).get_context_data(**kwargs)
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