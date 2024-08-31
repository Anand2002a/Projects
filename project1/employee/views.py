from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def homepage(request):
    return render(request,'index.html')