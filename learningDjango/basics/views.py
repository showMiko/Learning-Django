from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import Item 

# Create your views here.
def all_basic_view(request):
    items=Item.objects.all()
    # context={'items':items}
    return render(request, 'basics/all_basics.html',{'items':items})

def details_view(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    return render(request, 'basics/details.html', {'item':item})