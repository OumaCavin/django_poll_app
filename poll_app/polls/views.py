# Create your views here.
# from django.http import HttpResponse
# poll_app/poll/views.py¶

# polls/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def faq(request):
    return render(request, 'faq.html')
