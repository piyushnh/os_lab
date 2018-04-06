from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Event, Comment
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth import get_user_model
from .forms import CommentReplyForm

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
User = get_user_model()
# Create your views here.

class HomeView(TemplateView):
    template_name = 'blog/home.html'


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/posts.html'

class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'blog/events/events.html'

@user_passes_test(lambda u: u.is_superuser)
def ReplyComment(request, pk):
    parent = get_object_or_404(Comment, pk=pk)
    post = parent.post
    if request.method == "POST":
        form = CommentReplyForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.parent = parent
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentReplyForm()
    return render(request, 'blog/comment_reply_form.html', {'form': form})




    # def get_queryset(self):
    #     # super().get_queryset()
    #     return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
