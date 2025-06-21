from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .form import ProdutoForm

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def home(request):
    return render(request, 'home.html')
