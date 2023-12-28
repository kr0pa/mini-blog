from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Post

# Create your views here.
class BlogView(View):
    def get(self, request):
        posts = Post.objects.all()
        # return HttpResponse("Hello World!")
        
        return render(request, "home.html")
