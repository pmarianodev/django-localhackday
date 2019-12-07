from django.shortcuts import render
from ator.models import Ator

# Create your views here.
from filmes.models import Filme


'''def cadastrarFilme(request):
    listaDeAtores = Ator.objects.all()

    return render(request, 'cadastrarFilme.html', {'listaDeAtores': listaDeAtores})'''


'''def listarFilmes(request):
    listaDeFilmes = Filme.objects.all()

    return render(request, 'listarFilmes.html', {'listaDeFilmes': listaDeFilmes})'''
