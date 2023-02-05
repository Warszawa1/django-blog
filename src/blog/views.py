from django.shortcuts import render, get_object_or_404
from django.http import Http404 # longer version to display 404 errors

# Create your views here.
# Relative import
from .models import BlogPost

# GET -> 1 object
# filter -> [] objects

def blog_post_detail_page(request, slug):
    # queryset = BlogPost.objects.filter(slug=slug)# query -> database -> data -> django renders it
    # if queryset.count() == 0:
    #     raise Http404
    # obj = queryset.first()
    # Because slugs are all unique we can use this instead
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)