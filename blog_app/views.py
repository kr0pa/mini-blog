from django.shortcuts import render
from django.views import View
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
