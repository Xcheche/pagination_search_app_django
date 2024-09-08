from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    movies = Movies.objects.all()
    pagiantor = Paginator(movies, 3)
    page = request.GET.get("page")
    movies = pagiantor.get_page(page)
    context = {"movies": movies}
    return render(request, "dummy/index.html", context)
