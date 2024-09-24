from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import Category, Thread, Post


class CategoryTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "forum/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


@login_required
def show_threads(request, id):
    context = {
        "threads": Thread.objects.filter(category=id),
        "category": Category.objects.filter(id=id).first(),
    }
    return render(request, "forum/threads.html", context=context)


@login_required
def show_posts(request, thread_id):
    id = thread_id
    context = {
        "posts": Post.objects.filter(thread=id).order_by("-created_at"),
        "thread": Thread.objects.filter(id=id).first(),
    }
    return render(request, "forum/posts.html", context=context)
