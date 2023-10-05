import uuid
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from home.models import BannerImagesModel, MyCart
from product.models import OrderDetailModel, ProductCategoryModel, ProductModel
from django.contrib.auth.decorators import login_required
from product.forms import OrderDetailForm
from django.utils.decorators import method_decorator

# Create your views here.


class IndexView(View):
    
    template_name =  'home/index.html'

    def get(self, request):
        banner_images = BannerImagesModel.objects.filter(is_active=True)
        products = ProductModel.objects.all().order_by('id')[:5]
        if request.user.is_authenticated:
            user_cart = MyCart.objects.filter(user_id=request.user)
            result_list = [item.product_id for item in user_cart]
        else:
            result_list = []

        context = {
            'banner_images': banner_images,
            # 'main_feature_item': main_feature_item,
            # 'other_feature_item': other_feature_item,
            'products': products, 
            'user_cart': result_list
        }

        return render(request, self.template_name, context=  context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)




class AllCategoriesView(View):
    model  = ProductCategoryModel
    template_name = 'home/categories.html'

    def get(self, request):
        categories = self.model.objects.filter(is_active =  True)
        context  =  {
        'categories': categories
        }
        return render(request, self.template_name, context= context)



@method_decorator(login_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class MyPurchases(View):
    model = OrderDetailModel
    template_name  = 'home/mypurchases.html'

    def get(self, request):
        orders = OrderDetailModel.objects.filter(
        ordered_by=request.user).order_by('id')
        context = {
            'pruchases': orders
        }
        return render(request, 'home/mypurchases.html', context)






@login_required(login_url='/auth/login', redirect_field_name='ReturnUrl')
def PostCartView(request, id):
    if request.method == 'POST':
        try:
            # item = get_object_or_404(models.MyCart, id=id)
            item = MyCart.objects.filter(
                product_id=id, user_id=request.user)
            print('ITEM', item)
            if item:
                try:
                    item.delete()
                    return JsonResponse({
                        'status': 200,
                        'message': 'Cart deleted'
                    })
                except Exception as e:
                    print(e)
            else:
                try:
                    product_instance = ProductModel.objects.get(id=id)
                    MyCart.objects.create(
                        user_id=request.user, product_id=product_instance)
                except Exception as e:
                    print(e)
                return JsonResponse({
                    'status': 200,
                    'message': 'Cart added'
                })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'error_msg': e
            }, safe=False)
    else:
        return JsonResponse({
            'status': 'error',
            'error_msg': 'Method Not allowed'
        }, safe=False)


@login_required(login_url='/auth/login', redirect_field_name='ReturnUrl')
def MyCartPage(request):
    form = OrderDetailForm(request.POST or None)
    cart_items = MyCart.objects.filter(user_id=request.user, cart_status =  True)
    if request.method == 'POST':
        pay_now =  request.POST.get('pay_now')
        product_list = request.POST.getlist('product[]')
        print('product', product_list)
        if form.is_valid():
            data =  form.cleaned_data
            order_uuid  =  uuid.uuid4()
            for item in product_list:
                print('item', item)
                temp_order =  OrderDetailModel(**data)
                product = ProductModel.objects.get(id=item)
                temp_order.ordered_by = request.user
                temp_order.total_price = temp_order.quantity * product.price
                temp_order.product_id = product
                temp_order.order_uuid =  order_uuid
                if pay_now:
                    temp_order.payment_completed =  True
                temp_order.save()
                cart_items.delete()
            return redirect('home')


        else:
            context = {
                'cart_items': cart_items,
                'form': form
            }
            return render(request, 'home/mycart.html', context)

    context = {
        'cart_items': cart_items,
        'form': form
    }
    return render(request, 'home/mycart.html', context)


@login_required(login_url='/auth/login',  redirect_field_name='ReturnUrl')
def RemoveCartItem(request, id):
    item = MyCart.objects.get(id=id)
    if item:
        item.delete()
        return redirect('my_cart')

    else:
        return redirect('my_cart')
    
