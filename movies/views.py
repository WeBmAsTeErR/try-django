from django.shortcuts import render

from .models import Movie

def movie_search_view(request):
    query_dict = request.GET # this is a dictionary
    query = query_dict.get('query') # <input type='text' name='query'/>
 
    try:
        query = int(query_dict.get('query'))
    except:
        query = None
 
    movie_obj = None
    if query is not None:
        movie_obj = Movie.objects.get(id=query)
    context = {
        "object" : movie_obj,
    }
    return render(request, "movies/search.html", context=context)

def movie_detail_view(request, id=None):
    movie_obj = None
    if id is not None:
        movie_obj = Movie.objects.get(id=id)
    context = {
        "object":movie_obj,
    }
    return render(request, "movies/detail.html", context=context)