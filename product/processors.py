from home.models import MyCart

def cart_count(request):
    cart =  MyCart.objects.filter(user_id =  request.user).count()
    return {
        'cart_count': cart
    }
