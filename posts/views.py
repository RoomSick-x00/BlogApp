from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request): # function to take request
    posts = Post.objects.all() #takes all the objects from the Post to posts variable and then returns later to the render function
    return render(request, 'index.html', {'posts': posts})  # whenever the function index is called the page index.html is rendered

def post(request, pk):
    post = Post.objects.get(id = pk)
    return render(request, 'post.html', {'post': post})