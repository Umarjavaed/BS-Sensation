from django.shortcuts import render
from .models import Product
from .models import HomepageContent
from .models import Banner
from django.shortcuts import render, get_object_or_404
from .models import GaggleText
import random


def homepage(request):
    products = Product.objects.all()  # Fetch all products from the database
    content = HomepageContent.objects.first() 
    banner = Banner.objects.first() 
    return render(request, 'index.html', {'products': products, 'content': content, 'banner': banner})
    
def index2(request):
    return render(request, 'index2.html')


def index2_product(request, product_id):
    # Get the product by ID (assuming you have a Product model)
    product = get_object_or_404(Product, id=product_id)
    
    # Calculate the discounted price if a discount exists
    if product.discount:
        discounted_price = product.price - product.discount
    else:
        discounted_price = None  # If no discount exists, leave it as None
    
    try:
        content = GaggleText.objects.first()  # Assuming you will only have one instance to manage
    except GaggleText.DoesNotExist:
        content = None

    # Fetch all products, excluding the current product
    all_products = Product.objects.exclude(id=product_id)
    
    # Ensure at least 4 products are available
    if len(all_products) < 4:
        random_products = all_products
    else:
        random_products = random.sample(list(all_products), 4)  # Select 4 random products

    # Pass product data to the template
    return render(request, 'index2.html', {'product': product, 'discounted_price': discounted_price, 'content': content, 'products': random_products})

