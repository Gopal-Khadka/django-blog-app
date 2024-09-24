from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import Category, Thread, Post
from .forms import PostEditForm


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


@login_required
def edit_post(request, post_id):
    id = post_id
    form = PostEditForm(id=id)
    context = {
        "form": form,
        "endpoint": reverse(viewname="api:post-edit", kwargs={"id": post_id}),
    }
    return render(request, "forum/edit_post.html", context=context)

@login_required
def delete_post(request, post_id):
    context = {
        "post":Post.objects.filter(id=post_id).first(),
        "endpoint": reverse(viewname="api:post-delete", kwargs={"id": post_id}),
    }
    return render(request, "forum/delete_post.html", context=context)
