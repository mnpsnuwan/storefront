from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
    # Pull data from db
    # Transform
    # Send emails
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Nuwan!'})
