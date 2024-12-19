from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    album = models.ForeignKey(Album, related_name="photos", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photos/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
