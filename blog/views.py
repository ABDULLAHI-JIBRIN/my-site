from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import UpdateView, CreateView,DeleteView

def home(request):
    recent_post = Post.objects.order_by('date')[:2]
    return render(request,'home.html',{
        'recent_post':recent_post
    })

def about(request):
    information = Information.objects.all()
    return render(request,'about.html',{
        'information':information
    })


def resume(request):
    information = Information.objects.all()
    return render(request,'resume.html',{
        'information':information
    })



def blog(request):
    posts = Post.objects.all()
    recent_post = Post.objects.order_by('date')[:]
    return render(request,'blog.html',{
        'posts':posts,
        'recent_post':recent_post
    })


def post_detail_view(request,id):
    post = get_object_or_404(Post, id = id)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect('/')

    else:
        form = CommentForm()

    return render(request, 'post_detail.html',{
        'post':post,
        'form':form
    })

def reply_view(request, id):
    comment_one = get_object_or_404(comment, id = id)
    if request.method == 'POST':
        form = ReplyForm(request.POST or None)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.comment = comment_one
            form.save()
            return redirect('blog')

    else:
        form = ReplyForm()

    return render(request, 'reply.html',{
        'form':form
    })


class UpdatePost(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = [
        'title','category','image','content'
    ]
    template_name = 'update_post.html'
    success_message = f'Post updated successfully!'

    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.author:
            return True
        return False


class DeltePost(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'

    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.author:
            return True
        return False

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = [
        'title','category','image','content'
    ]
    
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def update_resume(request,id):
    information = get_object_or_404(Information, id = id)
    if request.method == 'POST':
        form = InformationForm(request.POST , instance = information )
        if form.is_valid():
            form.save()
            messages.success(request, f'Resume updated successfully!')
            return redirect('resume')

    else:

        form = InformationForm(instance = information)

    return render(request, 'update_resume.html',{
        'form':form
    })

def update_about(request,id):
    information = get_object_or_404(Information, id = id)
    if request.method == 'POST':
        form = InformationForm(request.POST , instance = information )
        if form.is_valid():
            form.save()
            messages.success(request, f'About updated successfully!')
            return redirect('resume')

    else:

        form = InformationForm(instance = information)

    return render(request, 'update_about.html',{
        'form':form
    })



