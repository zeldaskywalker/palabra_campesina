from django.urls import path

from . import views

urlpatterns = [
    path('', views.site_password_view, name='password'),
    path('inicio/', views.InicioView.as_view(), name='inicio'),
    path('galeria/', views.GaleriaOverallView.as_view(), name='galeria'),
    path('galeria/<int:row_id>/', views.GaleriaImageView.as_view(), name='galeria_image'),
    path('testimonios/', views.TestimoniosView.as_view(), name='testimonios'),
    path('sobre/', views.SobreView.as_view(), name='sobre'),
]