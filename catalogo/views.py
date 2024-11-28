from django.shortcuts import render, get_object_or_404, redirect
from .models import Videojuego, Comentario
from .forms import ComentarioForm
from django.contrib.auth.decorators import login_required

def catalogo(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'catalogo.html', {'videojuegos': videojuegos})

from django.http import JsonResponse

def filtrar(request):
    plataforma = request.GET.get('plataforma')
    genero = request.GET.get('género')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    buscar = request.GET.get('buscar')

    videojuegos = Videojuego.objects.all()

    if plataforma:
        videojuegos = videojuegos.filter(plataforma__icontains=plataforma)
    if genero:
        videojuegos = videojuegos.filter(género__icontains=genero)
    if precio_min:
        videojuegos = videojuegos.filter(precio__gte=precio_min)
    if precio_max:
        videojuegos = videojuegos.filter(precio__lte=precio_max)
    if buscar:
        videojuegos = videojuegos.filter(nombre__icontains=buscar)

    videojuegos_list = list(videojuegos.values('id', 'nombre', 'plataforma', 'género', 'precio', 'imagen'))

    return JsonResponse({'videojuegos': videojuegos_list})

def buscar(request):
    query = request.GET.get('buscar')
    videojuegos = Videojuego.objects.filter(nombre__icontains=query)
    return render(request, 'catalogo.html', {'videojuegos': videojuegos})

def detalles(request, id):
    videojuego = get_object_or_404(Videojuego, id=id)
    comentarios = Comentario.objects.filter(videojuego=videojuego)
    return render(request, 'detalles.html', {'videojuego': videojuego, 'comentarios': comentarios, 'user': request.user})

@login_required
def agregar_comentario(request, videojuego_id):
    videojuego = get_object_or_404(Videojuego, id=videojuego_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.videojuego = videojuego
            comentario.usuario = request.user
            comentario.save()
            return redirect('detalles', id=videojuego.id)
    else:
        form = ComentarioForm()
    return render(request, 'detalles.html', {'videojuego': videojuego, 'form': form})

def inicio(request):
    return redirect('catalogo')