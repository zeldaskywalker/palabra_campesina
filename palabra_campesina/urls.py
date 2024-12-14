from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('gallery/', views.GalleryOverallView.as_view(), name='gallery'),
    path('gallery/<int:row_id>/', views.GalleryImageView.as_view(), name='gallery_image'),
    path('stories/', views.StoriesArchiveView.as_view(), name='stories'),
    # path('story/', views.StoryView.as_view(), name='story'),
    path('about/', views.AboutView.as_view(), name='about'),
]