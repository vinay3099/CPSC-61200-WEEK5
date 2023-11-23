# helloworldapp/views.py
from django.shortcuts import render

def hello_world(request):
    context = {
        'message': 'Hello World!',
    }
    return render(request, 'hello_world.html', context)
