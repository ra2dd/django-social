from django.shortcuts import render
from django.views import generic
from posts.models import Post


class PostListView(generic.ListView):
    model = Post
