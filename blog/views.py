from django.core.context_processors import request
from django.shortcuts import render_to_response
from django.template.context import Context, RequestContext
from django.contrib import admin
from blog.models import Post
from django.shortcuts import render, get_object_or_404
from django_ajax.decorators import ajax


def home(request):

    c = Context({ "WHO": str(55+55)
    })
    return render_to_response("home.html", c, context_instance=RequestContext(request))


    from django.shortcuts import render, get_object_or_404
    from blog.models import Post

@ajax
def sayHello(request):
    print("hi");
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    print(posts);
    # now return the rendered template
    return  {'posts': posts}

def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})

def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})