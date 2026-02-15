from django.shortcuts import render, redirect, get_object_or_404
from home.models import Category
from home.models import Product

# Create your views here.


###Category####
def dashboard(request):
    return render(request, 'myadmin/dashboard.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'myadmin/category_list.html', {"categories": categories})

def category_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('category_list')

    return render(request, 'myadmin/category_add.html')

def category_edit(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        category.name = request.POST.get('name')
        category.save()
        return redirect('category_list')

    return render(request, 'myadmin/category_edit.html', {"category": category})

def category_delete(request, id):
    cat = get_object_or_404(Category, id=id)
    cat.delete()
    return redirect('category_list')




###PRODUCTS####
def product_list(request):
    Products = Product.objects.all()
    print("PRODUCT COUNT =", Products.count())  # DEBUG
    return render(request, 'myadmin/product_list.html', {"Products": Products})

def product_add(request):
    categories = Category.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')  

        category = Category.objects.get(id=category_id)

        Product.objects.create(
            name=name,
            price=price,
            description=description,
            category=category,
            image=image
        )

        return redirect('product_list')

    return render(request, 'myadmin/product_add.html', {"categories": categories})



def product_edit(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.name = request.POST.get('name')
        product.save()
        return redirect('product_list')
    
    return render(request, 'myadmin/product_edit.html', {"product": product})




def product_delete(request, id):
    pro = get_object_or_404(Product, id=id)
    pro.delete()
    return redirect('product_list')
