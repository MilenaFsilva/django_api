from .models import *
from rest_framework import serializers

#pega as inforções de python e converter a json

class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        many = True #se o many estive False ele retorna apenas um usário e se tiver True ele retorna uma Array com tds usuários
        model = Filmes
        fields = '__all__' #TODOS OS CAMPOS DO MODELS QUE ELE QUER CONVERTER
    
class AssinaturaSerializer(serializers.ModelSerializer):   
    class Meta:
        many = True #se o many estive False ele retorna apenas um usário e se tiver True ele retorna uma Array com tds usuários
        model = Assinatura
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):   
    class Meta:
        many = True #se o many estive False ele retorna apenas um usário e se tiver True ele retorna uma Array com tds usuários
        model = Categoria
        fields = '__all__'



class UsuarioSerializer(serializers.ModelSerializer):   
    class Meta:
        many = True #se o many estive False ele retorna apenas um usário e se tiver True ele retorna uma Array com tds usuários
        model = Usuario
        fields = '__all__'

class FavoritosSerializer(serializers.ModelSerializer):   
    class Meta:
        many = True #se o many estive False ele retorna apenas um usário e se tiver True ele retorna uma Array com tds usuários
        model = Favoritos
        fields = '__all__'

