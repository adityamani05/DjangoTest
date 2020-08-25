from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    initial_data = {
        "title": "This is initial tile"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data,
                       instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    product = Product.objects.get(id=1)
    context = {
        "title": product.title,
        "description": product.description,
    }
    return render(request, "products/product_detail.html", context)


def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "obj": obj,
    }
    return render(request, "products/product_detail.html", context)


def product_list(request):
    obj = Product.objects.all()
    context = {
        "objs": obj,
    }
    return render(request, "products/product_list.html", context)
