from django.urls import path
from .views import *

urlpatterns = [

    path("filmes/", FilmesAPIView.as_view(), name='filmes'),
    path('filmes/<int:pk>/',  FilmesAPIView.as_view(), name='filmesParameters'),
    
    path("categoria/", CategoriaAPIView.as_view(), name='categoria'), 
    path('categoria/<int:pk>/', CategoriaAPIView.as_view(), name='categoriaParameters'),
     
    path("assinatura/", AssinaturaAPIView.as_view(), name='assinatura'), 
    path('assinatura/<int:pk>/', AssinaturaAPIView.as_view(), name='assinaturaParameters'),
 
    path("usuario/", UsuarioAPIView.as_view(), name='usuario'), 
    path('usuario/<int:pk>/', UsuarioAPIView.as_view(), name='usuarioParameters'),

    path("favoritos/", FavoritosAPIView.as_view(), name='favoritos'), 
    path('favoritos/<int:pk>/', FavoritosAPIView.as_view(), name='favoritosParameters'),

]

