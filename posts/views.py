from django.shortcuts import render
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm

# Create your views here.

def posts_list(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)

        if form.is_valid():
            author = Author.objects.get(pk=int(form.cleaned_data['author']))
            data = form.cleaned_data.copy()
            data['author'] = author
            Post.objects.create(**data)

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

#def authors_list(request):
 #   authors = Author.objects.all()
  #  return render(
   #     request=request,
    #    template_name="maths/list.html",
    #    context={"author": authors}
    #)

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
