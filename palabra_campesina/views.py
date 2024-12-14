from django.views import generic
from django.shortcuts import render
from . import baserow

class HomeView(generic.TemplateView):
    template_name = 'home.html'

class GalleryOverallView(generic.ListView):
    template_name = 'gallery.html'
    data = baserow.get_gallery_all_images()

    def get_context_data(self, **kwargs):
        context = super(GalleryOverallView, self).get_context_data(**kwargs)
        context['data'] = self.data
        return context

    def get_queryset(self, **kwargs):
        return self.data

class GalleryImageView(generic.TemplateView):
    template_name = 'gallery_image.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryImageView, self).get_context_data(**kwargs)
        context['data'] = baserow.get_gallery_image_singular(context['row_id'])
        return context['data']
    
class StoriesArchiveView(generic.ListView):
    template_name = 'archive.html'
    data = baserow.get_stories_all()

    def get_context_data(self, **kwargs):
        context = super(StoriesArchiveView, self).get_context_data(**kwargs)
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
    
class AboutView(generic.TemplateView):
    template_name = 'about.html'