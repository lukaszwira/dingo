from django.urls import path
from .views import posts_list, post_details, authors_list, author_details

app_name="posts"
urlpatterns = [
    path('posts_list/', posts_list, name="list"),
    path('post_details/<int:id>', post_details, name="details"),
    path('authors_list/', authors_list, name="authors"),
    path('author_details/<int:id>', author_details, name="author"),
]
