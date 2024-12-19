from django.shortcuts import render, get_object_or_404, redirect

from .models import Album
from .forms import AlbumForm, PhotoForm


def index(request):
    return render(request, "index.html")


def album_list(request):
    albums = Album.objects.all()
    return render(request, "album_list.html", {"albums": albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "album_detail.html", {"album": album})


def create_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("album_list")
    else:
        form = AlbumForm()
    return render(request, "create_album.html", {"form": form})


def create_photo(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("album_list")
    else:
        form = PhotoForm()
    return render(request, "create_photo.html", {"form": form})
