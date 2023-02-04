from django.shortcuts import render

# Create your views here.
# Relative import
from .models import BlogPost

def blog_post_detail_page(request):
    obj = BlogPost.objects.get(id=2) # query -> database -> data -> django renders it
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)