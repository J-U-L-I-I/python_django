from django.shortcuts import render

# Create your views here.

def catalogo(request): 
    return render(request,'catalogo.html', {})
