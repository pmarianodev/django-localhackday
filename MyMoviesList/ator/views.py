from django.shortcuts import render


# Create your views here.
from ator.models import Ator
from filmes.models import Filme


'''def cadastrarAtor(request):
    return render(request, 'cadastrarAtor.html')'''


'''def atoresFilme(request, idFilme):
    filme = Filme.objects.get(id=idFilme)
    listaDeAtores = filme.atores.all()

    return render(request, 'listarAtores.html', {'listaDeAtores': listaDeAtores})'''


'''def listarAtores(request):
    listaDeAtores = Ator.objects.all()

    return render(request, 'listarAtores.html', {'listaDeAtores': listaDeAtores})'''
