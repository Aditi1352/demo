from turtle import title
from django.shortcuts import render

projects=[
    {
        'author':'Name1',
        'title':'Project Title',
        'approved_By':'TSM 1',
        'content':'......',
        'date_published':'....'
    },
      {
        'author':'Name2',
        'title':'Project Title',
        'approved_By':'TSM 2',
        'content':'......',
        'date_published':'....'
    },
      {
        'author':'Name3',
        'title':'Project Title',
        'approved_By':'TSM 3',
        'content':'......',
        'date_published':'....'
    }
]

# Create your views here.
def home(request):
    context={
        'projects':projects
        }
    return render(request,'app/home.html',context)
    

def about(request):
    return render(request,'app/about.html')

def login(request):
    return render(request,'app/login.html')

def signup(request):
    return render(request,'app/signup.html')

