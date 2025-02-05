from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Medicine, Category, Brand
# Create your views here.

def all_medicine(request):
    # Get filter parameters
    brand_ids =request.GET.get('brand',None)
    if brand_ids:
        brand_ids = list( map(int,str(request.GET.getlist('brand'))[2:-2].split(',')))
        
    category_ids = request.GET.getlist('category', None)
    if category_ids:
        category_ids = list( map(int,str(request.GET.getlist('category'))[2:-2].split(',')))
        
    min_price = request.GET.get('min_price', 100)
    max_price = request.GET.get('max_price', 1000)

    # Filter medicine based on parameters
    medicine = Medicine.objects.all()
    if brand_ids:
        medicine = medicine.filter(brand__id__in=brand_ids)
    if category_ids:
        medicine = medicine.filter(category__id__in=category_ids)
    if min_price and max_price:
        medicine = medicine.filter(price__gte=min_price, price__lte=max_price)
    #print(medicine)

    # Pagination
    paginator = Paginator(medicine, 6)  # Show 6 medicine per page
    page_number = request.GET.get('page',1)  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the page object
    objects= page_obj.object_list
    # Fetch all brands, categories for the filter sidebar
    brands = Brand.objects.all()
    categories = Category.objects.all()

    # Return the filtered data to the template
    return render(request, 'product/show_product.html', {
        'page_obj': page_obj,  # Pass the page object to the template
        'brands': brands,
        'categories': categories,
        'selected_brands': brand_ids,  # Pass selected brands to the template
        'selected_categories': category_ids,  # Pass selected categories to the template
        'min_price': min_price,  # Pass minimum price to the template
        'max_price': max_price,  # Pass maximum price to the template
        'objects':objects,
    })


def search_product(request):
    query = request.GET.get('q', '').strip() # Get search query
    
    medicine = Medicine.objects.filter(name__icontains=query) if query else None  # Filter medicine by name
    if not medicine:
        medicine = Medicine.objects.filter(description__icontains=query) if query else Medicine.objects.none()  
        
    # Pagination for search results
    paginator = Paginator(medicine, 6)  # Show 6 med per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Fetch all brands, categories, and colors for filters
    brands = Brand.objects.all()
    categories = Category.objects.all()

    return render(request, 'product/show_product.html', {
        'objects':page_obj.object_list,
        'page_obj': page_obj,
        'brands': brands,
        'categories': categories,
        'query': query,  # Pass the query to the template
    })


from django.shortcuts import render, get_object_or_404
from products.models import Medicine

def product_detail(request, product_id):
    # Get the product by ID
    product = get_object_or_404(Medicine, id=product_id)

    # Get similar products based on the brand
    similar_products = Medicine.objects.filter(brand=product.brand).exclude(id=product.id)

    return render(request, 'product/product.html', {
        'product': product,
        'similar_products': similar_products,
    })
    
    

