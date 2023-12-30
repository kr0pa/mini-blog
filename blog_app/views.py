from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from .models import Post
from .forms import PostForm

# Create your views here.
class BlogView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "home.html", {"posts": posts})
    
class BlogCreateView(View):
    template = "post_new.html"
    form = PostForm()
    
    def get(self, request):   
        return render(request, self.template, {"form": self.form})
    
    def post(self, request):
        form = PostForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("home")

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    
class BlogUpdateView(View):
    template = "post_new.html"
    
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        form = PostForm(instance=post)
        return render(request, self.template, {"form": form})
    
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        form = PostForm(request.POST, instance=post)
        
        if form.is_valid():
            form.save()
            return redirect("home")
        
        return render(request, self.template, {"form": form})