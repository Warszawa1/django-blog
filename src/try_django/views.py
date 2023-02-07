from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost

# what any given view function does:
def home_page(request):
    my_title = "Hello there..."
    qs = BlogPost.objects.all()[:5]
    context = {"title": "Welcome to Django Blog", 'blog_list': qs}
    # if request.user.is_authenticated:
    #     context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_rendered_doc = "<h1>{{title}}</h1>".format(title=my_title)
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About Us"})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Us",
        "form": form
    }
    return render(request, "form.html", context)


def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)



