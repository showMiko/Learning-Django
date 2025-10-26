from django.http import HttpResponse
from django.shortcuts import render # Used to render HTML templates

def home(request):
    # return HttpResponse("Hello, welcome to Learning Django!")
    return render(request, 'website/index.html')  # Renders the index.html template

def about(request):
    return HttpResponse("This is the About page of Learning Django.")

def contact(request):
    return HttpResponse("Contact us at  abc@gmail.com ")
