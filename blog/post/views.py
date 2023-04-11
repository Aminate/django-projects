from django.shortcuts import render
from .models import Post

# Create your views here.

def poats_list(request):
    queryset = Post.objects.all()  #это как список
    return render(request, 'listing.html', {'posts':queryset})
