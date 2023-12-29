from django.shortcuts import render
from django.views import View
from .models import Post

# Create your views here.
class BlogView(View):
    def get(self, request):
        posts = Post.objects.all()

        return render(request, "home.html", {"posts": posts})
    
class BlogCreateView(View):
    def get(self, request):
        template= "post_new.html"
        
        return render(request, self.template)
