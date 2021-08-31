from django.http import response
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.views import generic
from django.views.generic.base import TemplateView
from .models import Post
from django.http import HttpResponseRedirect
from .forms import CommmentForm
from taggit.models import Tag, TaggedItem
from django.db.models import Count, query
from django.urls import reverse
import json
import requests


# Class for Post List in Homepage
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5

        

def tag_post(request, tag_slug=None):
    template_name = 'tag_post.html'
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tags__in=[tag])
    return render(request, template_name, {'posts':posts, 'tag':tag})


#Function for Post View page
def post_detail(request, slug):
    template_name = 'post_detail.html'
    # get post object
    post = get_object_or_404(Post, slug=slug)
    # active parent
    comments = post.comments.filter(active=True)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommmentForm(data=request.POST)
        if comment_form.is_valid():

            # Create comment but don't save to database yet
            new_comment =comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            #Save the comment to the database
            new_comment.save()
    else :
        comment_form =CommmentForm()
    # List of simiilar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-created_on') [:6]

    return render(request, template_name, {'post': post,
                                        'comments': comments,
                                        'new_comment': new_comment,
                                        'comment_form': comment_form,
                                        'similar_posts': similar_posts})


def about_view(request):
    template_name = "about.html"
    return render(request, template_name)

def contact_view(request):
    template_name = "contact.html"
    return render(request, template_name)
