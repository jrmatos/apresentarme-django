from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name="ingredients", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class Card(models.Model):
    url = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=300, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    photo_url = models.CharField(max_length=100, blank=True)
    instagram_url = models.CharField(max_length=100, blank=True)
    facebook_url = models.CharField(max_length=100, blank=True)
    youtube_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.url