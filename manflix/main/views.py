from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from . serializer import *

class FilmesAPIView(APIView):

    #permission_classes = (IsAuthenticated,) #se tiver descomentada todo mundo tem acesso
    #pk variável pr acessar a rota 

    def get(self, request, pk=''): #se o frontend chamar a rota GET sem definir a pk ele devolver todas as informações e se definir o pk ele tras as informaçõse do pk

        if pk == '':
            filmes = Filmes.objects.all() #select.from usuarios
            serializer = FilmesSerializer(filmes, many=True) #transforma em json as inforções dos usuários
            return Response(serializer.data) #devolve os dados pro frontend todos em tranformados em json através do serializer
        else:
            filmes  = Filmes.objects.get(id=pk) #se informou o pk ele busca todos os usários com o mesmo id informado #selecct from usuario id tal (quero o usuário específico)
            filmes = FilmesSerializer(filmes)
            return Response(serializer.data)

    def post(self, request): #inserir

        serializer = FilmesSerializer(data=request.data, many=True) #cadastrar um novo usuario o fw vai devolver usuario em json e vai converter em python e guardar a variavel no serializer
        serializer.is_valid(raise_exception=True) #vem pra cá
        serializer.save() #salva
        
        return Response({"msg": "Inserido com sucesso"}) #se deu certo mandaa essa msg

        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''): #atualizar as informações já existentes

        filmes  = Filmes.objects.get(id=pk) #pegue o usuário que tnha esse id
        serializer = FilmesSerializer(filmes , data=request.data)#pega as inforçaões atualizadas do FW e antigas do BW  faça uma converção e se for válido
        serializer.is_valid(raise_exception=True) #se for válido
        serializer.save() #salva

        return Response(serializer.data)

    def delete(self, request, pk=''): #saiu da bosch foi pra Naza e tem excluir ele do Sitema

        filmes  = Filmes.objects.get(id=pk) #acha vê se existe  #select * from usuarios where id=39
        filmes .delete() #deletar

        return Response({"msg": "Apagado com sucesso"})


class CategoriaAPIView(APIView):

    #permission_classes = (IsAuthenticated,) #se tiver descomentada todo mundo tem acesso
    #pk variável pr acessar a rota 

    def get(self, request, pk=''): #se o frontend chamar a rota GET sem definir a pk ele devolver todas as informações e se definir o pk ele tras as informaçõse do pk

        if pk == '':
            categoria = Categoria.objects.all() #select.from usuarios
            serializer = CategoriaSerializer(categoria, many=True) #transforma em json as inforções dos usuários
            return Response(serializer.data) #devolve os dados pro frontend todos em tranformados em json através do serializer
        else:
            categoria = Categoria.objects.get(id=pk) #se informou o pk ele busca todos os usários com o mesmo id informado #selecct from usuario id tal (quero o usuário específico)
            serializer = CategoriaSerializer(categoria)
            return Response(serializer.data)

    def post(self, request): #inserir

        serializer = CategoriaSerializer(data=request.data, many=True) #cadastrar um novo usuario o fw vai devolver usuario em json e vai converter em python e guardar a variavel no serializer
        serializer.is_valid(raise_exception=True) #vem pra cá
        serializer.save() #salva
        
        return Response({"msg": "Inserido com sucesso"}) #se deu certo mandaa essa msg

        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''): #atualizar as informações já existentes

        categoria = Categoria.objects.get(id=pk) #pegue o usuário que tnha esse id
        serializer = CategoriaSerializer(materias, data=request.data)#pega as inforçaões atualizadas do FW e antigas do BW  faça uma converção e se for válido
        serializer.is_valid(raise_exception=True) #se for válido
        serializer.save() #salva

        return Response(serializer.data)

    def delete(self, request, pk=''): #saiu da bosch foi pra Naza e tem excluir ele do Sitema

        categoria = Categoria.objects.get(id=pk) #acha vê se existe  #select * from usuarios where id=39
        categoria.delete() #deletar

        return Response({"msg": "Apagado com sucesso"})


class AssinaturaAPIView(APIView):

    #permission_classes = (IsAuthenticated,) #se tiver descomentada todo mundo tem acesso
    #pk variável pr acessar a rota 

    def get(self, request, pk=''): #se o frontend chamar a rota GET sem definir a pk ele devolver todas as informações e se definir o pk ele tras as informaçõse do pk

        if pk == '':
            assinatura = Assinatura.objects.all() #select.from usuarios
            serializer = AssinaturaSerializer(assinatura, many=True) #transforma em json as inforções dos usuários
            return Response(serializer.data) #devolve os dados pro frontend todos em tranformados em json através do serializer
        else:
            assinatura = Assinatura.objects.get(id=pk) #se informou o pk ele busca todos os usários com o mesmo id informado #selecct from usuario id tal (quero o usuário específico)
            serializer = AssinaturaSerializer(assinatura)
            return Response(serializer.data)

    def post(self, request): #inserir

        serializer = AssinaturaSerializer(data=request.data, many=True) #cadastrar um novo usuario o fw vai devolver usuario em json e vai converter em python e guardar a variavel no serializer
        serializer.is_valid(raise_exception=True) #vem pra cá
        serializer.save() #salva
        
        return Response({"msg": "Inserido com sucesso"}) #se deu certo mandaa essa msg

        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''): #atualizar as informações já existentes

        assinatura = Assinatura.objects.get(id=pk) #pegue o usuário que tnha esse id
        serializer = AssinaturaSerializer(materias, data=request.data)#pega as inforçaões atualizadas do FW e antigas do BW  faça uma converção e se for válido
        serializer.is_valid(raise_exception=True) #se for válido
        serializer.save() #salva

        return Response(serializer.data)

    def delete(self, request, pk=''): #saiu da bosch foi pra Naza e tem excluir ele do Sitema

        assinatura = Assinatura.objects.get(id=pk) #acha vê se existe  #select * from usuarios where id=39
        assinatura.delete() #deletar

        return Response({"msg": "Apagado com sucesso"})


class UsuarioAPIView(APIView):

    #permission_classes = (IsAuthenticated,) #se tiver descomentada todo mundo tem acesso
    #pk variável pr acessar a rota 

    def get(self, request, pk=''): #se o frontend chamar a rota GET sem definir a pk ele devolver todas as informações e se definir o pk ele tras as informaçõse do pk

        if pk == '':
            usuario =  Usuario.objects.all() #select.from usuarios
            serializer =  UsuarioSerializer(usuario, many=True) #transforma em json as inforções dos usuários
            return Response(serializer.data) #devolve os dados pro frontend todos em tranformados em json através do serializer
        else:
            usuario =  Usuario.objects.get(id=pk) #se informou o pk ele busca todos os usários com o mesmo id informado #selecct from usuario id tal (quero o usuário específico)
            serializer =  UsuarioSerializer(usuario)
            return Response(serializer.data)

    def post(self, request): #inserir

        serializer =  UsuarioSerializer(data=request.data, many=True) #cadastrar um novo usuario o fw vai devolver usuario em json e vai converter em python e guardar a variavel no serializer
        serializer.is_valid(raise_exception=True) #vem pra cá
        serializer.save() #salva
        
        return Response({"msg": "Inserido com sucesso"}) #se deu certo mandaa essa msg

        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''): #atualizar as informações já existentes

        usuario =  Usuario.objects.get(id=pk) #pegue o usuário que tnha esse id
        serializer =  UsuarioSerializer(materias, data=request.data)#pega as inforçaões atualizadas do FW e antigas do BW  faça uma converção e se for válido
        serializer.is_valid(raise_exception=True) #se for válido
        serializer.save() #salva

        return Response(serializer.data)

    def delete(self, request, pk=''): #saiu da bosch foi pra Naza e tem excluir ele do Sitema

        usuario =  Usuario.objects.get(id=pk) #acha vê se existe  #select * from usuarios where id=39
        usuario.delete() #deletar

        return Response({"msg": "Apagado com sucesso"})

class FavoritosAPIView(APIView):

    #permission_classes = (IsAuthenticated,) #se tiver descomentada todo mundo tem acesso
    #pk variável pr acessar a rota 

    def get(self, request, pk=''): #se o frontend chamar a rota GET sem definir a pk ele devolver todas as informações e se definir o pk ele tras as informaçõse do pk

        if pk == '':
            favoritos =  Favoritos.objects.all() #select.from usuarios
            serializer =  FavoritosSerializer(favoritos, many=True) #transforma em json as inforções dos usuários
            return Response(serializer.data) #devolve os dados pro frontend todos em tranformados em json através do serializer
        else:
            favoritos =  Favoritos.objects.get(id=pk) #se informou o pk ele busca todos os usários com o mesmo id informado #selecct from usuario id tal (quero o usuário específico)
            serializer =  FavoritosSerializer(favoritos)
            return Response(serializer.data)

    def post(self, request): #inserir

        serializer = FavoritosSerializer(data=request.data, many=True) #cadastrar um novo usuario o fw vai devolver usuario em json e vai converter em python e guardar a variavel no serializer
        serializer.is_valid(raise_exception=True) #vem pra cá
        serializer.save() #salva
        
        return Response({"msg": "Inserido com sucesso"}) #se deu certo mandaa essa msg

        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''): #atualizar as informações já existentes

        usuario =  Favoritos.objects.get(id=pk) #pegue o usuário que tnha esse id
        serializer =  FavoritosSerializer(materias, data=request.data)#pega as inforçaões atualizadas do FW e antigas do BW  faça uma converção e se for válido
        serializer.is_valid(raise_exception=True) #se for válido
        serializer.save() #salva

        return Response(serializer.data)

    def delete(self, request, pk=''): #saiu da bosch foi pra Naza e tem excluir ele do Sitema

        favoritos =  Favoritos.objects.get(id=pk) #acha vê se existe  #select * from usuarios where id=39
        favoritos.delete() #deletar

        return Response({"msg": "Apagado com sucesso"})