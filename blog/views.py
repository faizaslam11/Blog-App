from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post


# posts= [
#     {
#         'author': 'Mohd Faiz Aslam',
#         'title' : 'The Darkest Night',
#         'content':'My First Night',
#         'date' :'22/08/2020',
#     },
#     {
#         'author': 'Mohd Amaan Khan',
#         'title' : 'The lonely Night',
#         'content':'Feelings of being Alone',
#         'date' :'15/07/2020',
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()  
    }
    return render(request,'blog/home.html', context)

class PostListView(ListView):
    model= Post 
    template_name = 'blog/home.html'
    context_object_name= 'posts'
    ordering = ['-date']

class PostDetailView(DetailView):
    model= Post 
    

class PostCreateView(DetailView):
    model = Post
    fields = ['title', 'content']
    

def about(request):
    return render(request,'blog/about.html', {'Title' : 'About'})

