from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    movies = Movies.objects.all()
    
    #Search logic
    movie_name = request.GET.get('movie_name')
  
 
    if movie_name != '' and movie_name is not None:
        movies= movies.filter(name__icontains=movie_name)
        
  
    # End of search logic
    
    #Paginator
    pagiantor = Paginator(movies, 3)
    page = request.GET.get("page")
    movies = pagiantor.get_page(page)
    # End of paginator
    context = {"movies": movies}
    return render(request, "dummy/index.html", context)
