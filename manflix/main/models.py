from django.db import models

class Categoria(models.Model): #vai virar uma tabela no banco DE DADOS
 
    nome = models.CharField(max_length=55)

    def __str__(self):    
        return self.nome


class Categoria(models.Model): #vai virar uma tabela no banco DE DADOS
 
    nome = models.CharField(max_length=55)

    def __str__(self):    
        return self.nome

class Filmes(models.Model): #vai virar uma tabela no banco DE DADOS

    nome = models.CharField(max_length=55)
    categoria_fk = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):    
        return self.nome

class Assinatura(models.Model): #vai virar uma tabela no banco DE DADOS
 
    nome = models.CharField(max_length=55)
    valor = models.IntegerField() 

    def __str__(self):    
        return self.nome



class Usuario(models.Model): #vai virar uma tabela no banco DE DADOS
 
    nome = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    fone = models.CharField(max_length=55)
    status = models.BooleanField()
    assinatura_fk = models.name = models.ForeignKey(Assinatura, on_delete=models.CASCADE)

    def __str__(self):    
        return self.nome

class Favoritos(models.Model): #vai virar uma tabela no banco DE DADOS
 
    filmes_fk = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    usuario_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE)

   