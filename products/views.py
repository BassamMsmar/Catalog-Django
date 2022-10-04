from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from .models import Prducts
from .forms import AddProductForm

# Create your views here
def products_list(request, pk):
    # section = Sections.objects.filter(pk=pk)
    product = Prducts.objects.all()
    context ={
        'product':product,
        'pk': int(pk),
        }
    return render(request, 'products/products-list.html', context)

def add_product(request):
    # prducts = Prducts.objects.all()
    if request.method == 'POST':
        form = AddProductForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('sections_list')
    else:
            form = AddProductForm()
   
    context={'form':form}
    return render (request, 'products/add_product.html', context)


def edit_product(request, pk):
    prducts = get_object_or_404(Prducts, pk=pk)
    if request.method == 'POST':
        form = AddProductForm(request.POST,request.FILES, instance=prducts)
        
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
            form = AddProductForm(instance=prducts)
   
    context={'form':form}
    return render (request, 'products/add_product.html', context)