from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import Item, Tag
from .forms import ItemForm

# Create your views here.
def all_basic_view(request):
    items=Item.objects.all()
    # context={'items':items}
    return render(request, 'basics/all_basics.html',{'items':items})

def details_view(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    return render(request, 'basics/details.html', {'item':item})

def forms_view(request):
    forms=None
    if request.method=="POST":
        forms=ItemForm(request.POST)
        if forms.is_valid():
            cleaned_item_data=forms.cleaned_data['name'] # Accessing the selected value and cleaning it 
            print(forms.cleaned_data)
            data_tags=Tag.objects.filter(items=cleaned_item_data)
    else:
        forms=ItemForm()
        data_tags=None
    # Forms have multiple cases
    # Render a Form and no form is passed.
    # 2nd case is when user fills the form and submits it.
    return render(request, 'basics/forms_content.html',{'forms':forms, 'data_tags':data_tags})