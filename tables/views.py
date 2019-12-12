from tables.models import Genre
from django.shortcuts import render


def show_genres(request):
    return render(request, "genres.html", {'genres': Genre.objects.all()})
