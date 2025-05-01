from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    login_url = reverse_lazy('login')
    
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    
class CategoryListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/post_category_list.html'
    context_object_name = 'posts'
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
        categoria = self.kwargs['categoria']
        return Post.objects.filter(category=categoria)
     
@login_required(login_url='login')
def dashboard(request):
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'posts/dashboard.html', {'user_posts': user_posts})