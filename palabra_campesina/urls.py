from django.urls import path

from . import views

urlpatterns = [
    path('', views.contraseña_or_password_view, name='contraseña_or_password'),

    # Español
    path('inicio/', views.InicioView.as_view(), name='inicio'),
    path('galeria/', views.GaleriaOverallView.as_view(), name='galeria'),
    path('galeria/<int:row_id>/', views.GaleriaImageView.as_view(), name='galeria_image'),
    path('testimonios/', views.TestimoniosView.as_view(), name='testimonios'),
    path('testimonio/<int:row_id>', views.TestimonioView.as_view(), name='testimonio'),
    path('sobre/', views.SobreView.as_view(), name='sobre'),

    # English
    path('home/', views.HomeView.as_view(), name='home'),
    path('gallery/', views.GalleryOverallView.as_view(), name='gallery'),
    path('gallery/<int:row_id>/', views.GalleryImageView.as_view(), name='gallery_image'),
    path('testimonies/', views.TestimoniesView.as_view(), name='testimonies'),
    path('testimony/<int:row_id>', views.TestimonyView.as_view(), name='testimony'),
    path('about/', views.AboutView.as_view(), name='about'),
]