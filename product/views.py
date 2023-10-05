from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from ecommerce import renderers

from home.models import MyCart
from .forms import InventoryForm, OrderDetailForm, ProductCategoryForm, ProductForm, ProductImageFormSet
from django.shortcuts import get_object_or_404

from product.models import InventoryModel, OrderDetailModel, ProductModel, ProductCategoryModel
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


@method_decorator(staff_member_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class ManageProductView(View):
    template_name  =  'siteadmin/product.html'    

    def get(self, request):
        product_data = ProductModel.objects.all()
        context =  {
            'product_data': product_data
        }
        return render(request, self.template_name, context=context)


@method_decorator(staff_member_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class AddEditProductView(View):
    template_name =  'siteadmin/addform.html'

    def get(self,  request, product_id =  None):

        if product_id is not None:
            product_instance  = get_object_or_404(ProductModel, id  =  product_id)
            product_form = ProductForm(instance =  product_instance, prefix='product')
            image_formset = ProductImageFormSet(instance =  product_instance, prefix='image')
            print(dir(image_formset))
            print( 'ln_33',image_formset.as_p())
        else:
            product_form = ProductForm(prefix='product')
            image_formset = ProductImageFormSet(prefix='image')

        context =  {
            'action_url': 'add_product',
            'form_title': 'Manage Product', 
            'form': product_form, 
            'product_form': product_form, 
            'image_formset': image_formset
        }
        return render(request, self.template_name, context= context)

    def post(self,  request, product_id = None):

        if product_id is not None:
            product_instance  = get_object_or_404(ProductModel, id  =  product_id)
            product_form = ProductForm(request.POST, instance =  product_instance,  prefix='product')
            image_formset = ProductImageFormSet(request.POST, request.FILES, instance =  product_instance, prefix='image')
        else:
            product_form = ProductForm(request.POST, prefix='product')
            image_formset = ProductImageFormSet(request.POST, request.FILES, prefix='image')


        context =  {
            'action_url': 'add_product',
            'form_title': 'Manage Product', 
            'form': product_form, 
            'product_form': product_form, 
            'image_formset': image_formset
        }

        if product_form.is_valid() and image_formset.is_valid():
            product = product_form.save()
            image_formset.instance = product
            image_formset.save()
            return redirect('manage_product')
        
        return render(request, self.template_name,context=context)


@method_decorator(staff_member_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class ManageCategoryView(View):
    template_name =  'siteadmin/category.html'
    model  =  ProductCategoryModel


    def get(self, request):
        category_data = self.model.objects.all()
        context = {
            'category_data': category_data
        }
        return render(request, self.template_name, context=context)
    


@method_decorator(staff_member_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class AddEditCategoryView(View):
    model  =  ProductCategoryModel
    template_name =  'siteadmin/addform.html'
    form  = ProductCategoryForm

    def get(self, request, category_id =  None):
        
        if category_id is not None:
            category_instance =  get_object_or_404(self.model, id  =  category_id)
            category_form = self.form(instance  =  category_instance)
        else:
            category_form = self.form()

        context =  {
            'form_title': 'Manage Category', 
            'form': category_form, 
        }
        return render(request, self.template_name, context=context)

    def post(self, request, category_id  = None):
        if category_id is not None:
            category_instance =  get_object_or_404(self.model, id  =  category_id)
            category_form = self.form(request.POST or None, instance  =  category_instance)

        else:
            category_form = self.form(request.POST)
        

        context =  {
            'form_title': 'Manage Category', 
            'form': category_form, 
        }

        if category_form.is_valid():
            category_form.save()
            return redirect('manage_category')
        
        return render(request, self.template_name,context=context)




@method_decorator(staff_member_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class ManageInventoryView(View):
    template_name  =  'siteadmin/inventory.html'
    

    def get(self, request):
        inventory_data =  InventoryModel.objects.all()
        context  = {
            'inventory_data': inventory_data, 
        }
        return render(request, self.template_name, context=context)
    


@method_decorator(staff_member_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class AddEditInventoryView(View):
    form_model  =  InventoryForm
    model  = InventoryModel 
    template_name = 'siteadmin/addform.html'


    def get(self, request, inventory_id  =  None):
        if inventory_id is not None:
            inventory_instance  =  get_object_or_404(self.model, id =  inventory_id)
            inventory_form  =  self.form_model(instace =  inventory_instance)
        else:
            inventory_form =  self.form_model()

        context = {
            'form_title': 'Manage Inventory', 
            'form': inventory_form, 
        }
        return render(request, self.template_name, context=   context)



    def post(self, request, inventory_id =  None):
        
        if inventory_id is not None:
            inventory_instance  = get_object_or_404(self.model, id  = inventory_id)
            inventory_form =  self.form_model(request.POST  , request.FILES, instance  = inventory_instance)    

        else:
            inventory_form   =  self.form_model(request.POST  , request.FILES)


        context = {
            'form_title': 'Manage Inventory', 
            'form': inventory_form, 
        }

        if inventory_form.is_valid():
            inventory_form.save(context  =  request)
            return redirect('manage_inventory')
        
        return render(request, self.template_name, context=context)



class CategoryProductView(View):


    def get(self, request, category_url):
        from_price = request.GET.get('from_price')
        to_price = request.GET.get('to_price')
        page = request.GET.get('page')

        try:
            category = get_object_or_404(
                ProductCategoryModel, category_url_name=category_url)
        except Exception as e:
            return render(request, '404.html')

        product_instance = category.products.all()

        if request.user.is_authenticated:
            user_cart = MyCart.objects.filter(user_id=request.user)
            result_list = [item.product_id for item in user_cart]
        else:
            result_list = []

        if from_price:
            product_instance = product_instance.filter(price__gte=from_price)

        if to_price:
            product_instance = product_instance.filter(price__lte=to_price)

        all_products = Paginator(product_instance, 2)
        try:
            products = all_products.page(page)
        except PageNotAnInteger:
            products = all_products.page(1)
        except EmptyPage:
            products - all_products.page(all_products.num_pages)

        context = {'category': category,
                'products': products, 'user_cart': result_list}
        return render(request, 'products/product.html', context)



class ViewProductPage(View):
    model  = ProductModel
    template_name  = 'products/viewproduct.html'
    def get(self, request, slug):
        product  =  get_object_or_404(self.model, slug=slug)
        context = {
        'product': product,
    }   
        return render(request, self.template_name, context=context)



@method_decorator(login_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class CheckoutView(View):
    model =  ProductModel
    template  = 'products/checkout.html'
    sucuess_template  = 'products/ordersucess.html'
    form_model = OrderDetailForm

    def get(self, request, slug):
        product  = get_object_or_404(self.model, slug=slug)
        data = {
            'product': product,
            'form': self.form_model
        }
        return render(request, self.template, context=data)
    

    def post(self, request, slug):
        form  = self.form_model(request.POST, request.FILES)
        product =  get_object_or_404(self.model, slug= slug)
        pay_now =  request.POST.get('pay_now')
        if form.is_valid():
            newfrom =   form.save(commit=False)
            newfrom.ordered_by = request.user
            newfrom.total_price = newfrom.quantity  *  product.price
            newfrom.product_id = product
            if pay_now:
                newfrom.payment_completed  =  True
            newfrom.save()
            messages.success(request, 'Checkout Successfully')
            return redirect('home')
        
        context = {
            'product': product,
            'form': form
        }
        return render(request, self.template, context= context)

        


class ListProductView(View):
    template_name = 'products/product.html'
    model =  ProductModel

    def get(self, request):
        page = request.GET.get('page')
        from_price = request.GET.get('from_price')
        to_price = request.GET.get('to_price')
        product_instance = self.model.objects.prefetch_related('images').all()
        if request.user.is_authenticated:
            user_cart = MyCart.objects.filter(user_id=request.user)
            result_list = [item.product_id for item in user_cart]
        else:
            result_list = []

        if from_price:
            product_instance = product_instance.filter(price__gte=from_price)

        if to_price:
            product_instance = product_instance.filter(price__lte=to_price)

        all_products = Paginator(product_instance, 12)
        try:
            products = all_products.page(page)
        except PageNotAnInteger:
            products = all_products.page(1)
        except EmptyPage:
            products = all_products.page(all_products.num_pages)

        context = {
            'products': products,  'user_cart': result_list
        }
        return render(request, self.template_name, context)

    




login_required(login_url='auth/login', redirect_field_name='ReturnUrl')
def PrintReceipt(request, order_uuid):
    orders  =  OrderDetailModel.objects.filter(order_uuid  =  order_uuid)
    total =  0

    for item in orders:
        total += item.total_price
    context = {
        'request': request, 
        'orders':orders, 
        'total_price': total
    }
    
    response = renderers.render_to_pdf("products/receipt.html", context)
    if response.status_code == 404:
        raise Http404("Invoice not found")

    filename = f"Invoice_{order_uuid}.pdf"
    content = f"inline; filename={filename}"
    download = request.GET.get("download")
    if download:
        content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content
    return response

    # return render(request, 'products/receipt.html', context=context)