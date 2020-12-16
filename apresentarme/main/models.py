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
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=300)
    phone = models.CharField(max_length=100)
    photoUrl = models.CharField(max_length=100)
    instagramUrl = models.CharField(max_length=100)
    facebookUrl = models.CharField(max_length=100)
    youtubeUrl = models.CharField(max_length=100)

    def __str__(self):
        return self.url