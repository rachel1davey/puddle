from django.shortcuts import render
from item.models import Category, Item
# Create your views here.
def index(request):
    items = Item.objects.filter(isSold=False).order_by('-created_at')[0:6]
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')