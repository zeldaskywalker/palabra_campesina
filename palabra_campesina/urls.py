from django.urls import path

from . import views

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('galeria/', views.GaleriaOverallView.as_view(), name='galeria'),
    path('galeria/<int:row_id>/', views.GaleriaImageView.as_view(), name='galeria_image'),
    path('historias/', views.HistoriasView.as_view(), name='historias'),
    # path('story/', views.StoryView.as_view(), name='story'),
    path('sobre/', views.SobreView.as_view(), name='sobre'),
]