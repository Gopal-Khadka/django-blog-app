from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

from .models import Category, Thread, Post


class CategoryTemplateView(TemplateView):
    template_name = "forum/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


def show_threads(request, id):
    context = {
        "threads": Thread.objects.filter(category=id),
        "category": Category.objects.filter(id=id).first(),
    }
    return render(request, "forum/threads.html", context=context)


def show_posts(request, cat_id, thread_id):
    id = thread_id
    context = {
        "posts": Post.objects.filter(thread=id),
        "thread": Thread.objects.filter(id=id).first(),
    }
    return render(request, "forum/posts.html", context=context)
