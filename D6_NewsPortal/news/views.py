from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostsList (ListView):
    model = Post
    ordering = '-created_on'
    template_name = 'posts.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
