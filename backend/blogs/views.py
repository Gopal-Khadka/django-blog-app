from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from blogs.models import BlogPost
from blogs.forms import ContactForm, CreateBlogForm
from blogs.utils import get_share_links

def index(request):
    return render(request, "blogs/index.html")


def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("blogs:index")
    else:
        contact_form = ContactForm()
    return render(request, "blogs/contact.html", {"form": contact_form})


def about(request):
    return render(request, "blogs/about.html")


def blogs(request):

    return render(request, "blogs/blogs.html")


@login_required
def create_blogs(request):

    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            blog = form.save(
                commit=False
            )  # Save the blog without committing to the database yet
            blog.author = (
                request.user.author
            )  # Set the author field to the current user
            blog.save()  # Save the blog with all form data, including the image
            blog.tags.set(request.POST.getlist("tags"))
            return redirect("blogs:blogs-show", slug=blog.slug)
    else:
        form = CreateBlogForm(user=request.user)
    return render(
        request,
        "blogs/create_blogs.html",
        context={"form": form},
    )


def show_blogs(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    facebook_url, twitter_url,whatsapp_url,linkedin_url = get_share_links(request,post)
    return render(request, "blogs/show_blogs.html", context={
        "slug": slug,
        'facebook_url': facebook_url,
        'twitter_url': twitter_url,
        'whatsapp_url': whatsapp_url,
        'linkedin_url': linkedin_url,
        })


def search_blogs(request):
    return render(request, "blogs/search_blogs.html")


@login_required(login_url="blogs:login")
def discussion(request):
    return render(request, "blogs/discussion.html")


def logInUser(request):
    if request.user.is_authenticated:
        return redirect("blogs:index")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user=user)
            return redirect("blogs:index")
        else:
            return redirect("blogs:login")
    return render(request, "blogs/login.html")


def register(request):
    return render(request, "blogs/register.html")


def logOutUser(request):
    logout(request)
    return redirect("blogs:index")
