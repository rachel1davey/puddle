from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from django.db.models import Q
from .forms import NewItemForm, EditItemForm

# Create your views here.

def browse(request):
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    items = Item.objects.filter(isSold=False)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query))
    return render(request, 'item/browse.html', {
        'items': items,
        'query': query,
        'categories': categories
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, isSold=False).exclude(pk=item.pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            # Redirect to the detail view of the newly created item
            return redirect('item:detail', pk=item.pk)
        # If the form is not valid, it will clear the form and show a new one
    else:
            form = NewItemForm()
            
    form = NewItemForm()
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item'
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            # Redirect to the detail view of the newly created item
            return redirect('item:detail', pk=item.pk)
        # If the form is not valid, it will clear the form and show a new one
    else:
        form = EditItemForm(instance=item)
 
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item'
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

