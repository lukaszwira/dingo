from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'posts.Author',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f"id:{self.id}, title={self.title} content={self.content}"

class Author(models.Model):
    nick = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return f"nick: {self.nick} | email: {self.email}"
        