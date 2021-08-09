from django.shortcuts import render
import requests
import json
from .forms import SearchForm


API_KEY = "33b7bb6df0c945683fa7eb37dbf16663"


def home(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        search_word = request.POST.get("search")
        if form.is_valid():
            url = (
                "https://api.themoviedb.org/3/search/movie?api_key="
                + API_KEY
                + "&query="
                + search_word
            )
            response = requests.get(url)
            resdata = response.text
            obj = json.loads(resdata)
            obj = obj["results"]
            return render(request, "search.html", {"obj": obj})
    else:
        form = SearchForm()
        url = "https://api.themoviedb.org/3/trending/movie/week?api_key=" + API_KEY
        response = requests.get(url)
        resdata = response.text
        obj = json.loads(resdata)
        obj = obj["results"]
        return render(request, "index.html", {"obj": obj, "form": form})


def detail(request, movie_id):
    url = "https://api.themoviedb.org/3/movie/" + movie_id + "?api_key=" + API_KEY
    response = requests.get(url)
    resdata = response.text
    return render(request, "detail.html", {"resdata": resdata})
