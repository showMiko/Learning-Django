from django.shortcuts import render

# Create your views here.
def all_basic_view(request):
    return render(request, 'basics/all_basics.html')