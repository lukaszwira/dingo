from django.urls import path
from .views import posts_list, post_details, authors_list, author_details

app_name="posts"
urlpatterns = [
    path('posts/', posts_list, name="list"),
    path('posts/<int:id>', post_details, name="details"),
    path('authors/', authors_list, name="authors"),
    path('authors/<int:id>', author_details, name="author"),
]
