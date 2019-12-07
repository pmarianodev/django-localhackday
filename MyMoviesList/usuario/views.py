from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from ator.models import Ator
from filmes.models import Filme


'''def efetuaLogin(request):
    if request.POST:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'incorreta': True,
                                                  'request': request})

    return render(request, 'login.html')'''


'''def home(request):
    listaDeFilmes = Filme.objects.all()

    return render(request, 'paginaInicial.html', {'listaDeFilmes': listaDeFilmes,
                                                  'qntFilmes': len(listaDeFilmes)})'''
