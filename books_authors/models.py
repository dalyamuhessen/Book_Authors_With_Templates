from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc  = models.CharField(max_length=45)

    def __str__(self):
        return self.title
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    notes      = models.TextField(default="")
    books      = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"