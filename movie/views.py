from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Película agregada exitosamente.')
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie/add_movie.html', {'form': form})

def about(request):
    return render(request, 'movie/about.html')
