from django.http import HttpResponse
from django.template.loader import render_to_string
from movies.models import Movie
import random
 
def home_view(request):
   
    rand_int = random.randint(1, 3) #rand_id = 1, 2 or 3
    movie = Movie.objects.get(id= rand_int)
    movie_queryset = Movie.objects.all()
 
    context = {
        "movie_list": movie_queryset,
        "id" : movie.id,
        "title" : movie.title,
        "content" : movie.content
    }
 
    HTML_STRING = render_to_string("home-view.html", context=context)
 
    return HttpResponse(HTML_STRING)