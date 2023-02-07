from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import Http404# longer version to display 404 errors

# Create your views here.
# Relative import
from .forms import BlogPostForm, BlogPostModelForm
from .models import BlogPost

# GET -> 1 object
# filter -> [] objects

# def blog_post_detail_page(request, slug):
#     print("DJANGO SAYS", request.method, request.path, request.user)
    # obj = BlogPost.objects.get(slug=slug)
    # queryset = BlogPost.objects.filter(slug=slug)# query -> database -> data -> django renders it
    # if queryset.count() == 0:
    #     raise Http404
    # obj = queryset.first()
    # Because slugs are all unique we can use this instead
    # obj = get_object_or_404(BlogPost, slug=slug)
    # template_name = 'detail.html'
    # context = {"object": obj}
    # return render(request, template_name, context)


# CRUD (Create, Retrieve, Update, Delete)
def blog_post_list_view(request):
    # list out objects
    qs = BlogPost.objects.all().published() # queryset -> list of python objects
    # could be search
    # qs = BlogPost.objects.filter(title__icontains='Hola')
    # now = timezone.now()
    # ONLY SHOWS THE POSTS THAT ARE PUBLISHED
    # qs = BlogPost.objects.filter(publish_date__gte=now)
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct() #so it does not have duplicatesl
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    # create objects
    # ? use a form
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {"title": f"Update {obj.title}", 'form': form}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)


