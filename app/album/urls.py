from django.urls import path

from .views import album_list, album_detail, create_album, create_photo

urlpatterns = [
    path("", album_list, name="album_list"),
    path("<int:pk>/", album_detail, name="album_detail"),
    path("create/", create_album, name="create_album"),
    path("photo/create/", create_photo, name="create_photo"),
]
