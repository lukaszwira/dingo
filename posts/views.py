from django.shortcuts import render
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm
from django.contrib import messages

# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    form = PostForm()
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Dodano nowy Post!!"
            )

    form = PostForm()
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/list.html",
        context={
            "posts": posts,
            "form": form,
        }   
    )

def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/details.html",
        context={"post": post}
    )

def authors_list(request):
    if request.method == "POST":
        form = AuthorForm(data=request.POST)

        if form.is_valid():
            data = form.cleaned_data.copy()
            Author.objects.create(**data)

    form = AuthorForm()
    authors = Author.objects.all()
    return render(
        request=request,
        template_name="posts/author.html",
        context={
            "author": authors,
            "form": form,
        }   
    )

def author_details(request, id):
    author = Author.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/author_details.html",
        context={"author": author}
    )
