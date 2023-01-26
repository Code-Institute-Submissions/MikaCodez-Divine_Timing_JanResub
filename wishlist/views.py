from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
from wishlist.models import wishlist

# Create your views here.

def view_wishlist(request):
    """ A view that renders the Wishlist contents page """

    users_wishlist = wishlist.objects.get(user=request.user)

    context = {
        'wishlist': users_wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)



def add_to_wishlist(request, item_id):
    """ Add a product to the Wish List """

    user_wishlist, created = wishlist.objects.get_or_create( user=request.user)
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    user_wishlist.products.add(product)
    messages.success(request, f'Added {product.name} to wishlist')
    print("USER WISHLIST :", user_wishlist.products)

    return redirect(redirect_url)
    

def adjust_wishlist(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    wishlist = request.session.get('wishlist', {})
    messages.success(request, f'Added {product.name} to wishlist')

    request.session['wishlist'] = wishlist
    return redirect(reverse('view_wishlist'))


def remove_from_wishlist(request, item_id):
    """Remove the item from the shopping wishlist"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        wishlist = request.session.get('wishlist', {})
        messages.success(request, f'Added {product.name} to wishlist')

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)