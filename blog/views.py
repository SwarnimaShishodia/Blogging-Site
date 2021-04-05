from django.shortcuts import render

# Create your views here.

#HOME
def home(request):
    return render(request, 'blog/home.html')

#ABOUT
def about(request):
    return render(request, 'about/home.html')