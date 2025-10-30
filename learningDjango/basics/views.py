from django.shortcuts import render
from .models import Item
# Create your views here.
def all_basic_view(request):
    items=Item.objects.all()
    # context={'items':items}
    return render(request, 'basics/all_basics.html',{'items':items})