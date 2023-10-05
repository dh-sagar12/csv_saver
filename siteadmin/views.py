from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from home.forms import BannerImageForm
from product.forms import InventoryForm
from product.models import *
from home.models import BannerImagesModel
from .forms import OrderDetailsFormAdminSide
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@method_decorator(staff_member_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class DashboardView(View):
    template_name = 'siteadmin/home.html'


    def get(self, request):
        return render(request, self.template_name)


@method_decorator(staff_member_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class SettingView(View):
    template_name = 'siteadmin/setting.html'

    def get(self, request):
        return render(request, self.template_name)

@method_decorator(staff_member_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class ManageBannerImageView(View):
    template_name = 'siteadmin/banner.html'
    model =  BannerImagesModel


    def get(self, request):
        banner_data = self.model.objects.all()
        context =  {
            'banners_data': banner_data
        }
        return render(request, self.template_name, context=context)

@method_decorator(staff_member_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class AddEditBannerImages(View):
    template_name =  'siteadmin/addform.html'
    model =  BannerImagesModel
    form_model  = BannerImageForm

    def get(self, request, banner_id =  None):
        if banner_id is not None:
            banner_instance  = get_object_or_404(BannerImagesModel, id = banner_id)
            banner_form   =  self.form_model(instance =  banner_instance)         
        else:
            banner_form  =  self.form_model()

        context =  {
            'form_title': 'Manage Banner Images', 
            'form': banner_form, 
        }
        return render(request, self.template_name, context = context)
    
    def post(self, request, banner_id =  None):
        if banner_id is not None:
            banner_instance  = get_object_or_404(BannerImagesModel, id =  banner_instance)
            banner_form  =  self.form_model(request.POST, request.FILES, instance  = banner_instance)
        else:
            banner_form  = self.form_model(request.POST, request.FILES)
        
        context = {
            'form_title': 'Manage Banner Images', 
            'form': banner_form, 
        }

        if banner_form.is_valid():
            banner_form.save()
            return redirect('manage_banner_images')
        
        return render(request, self.template_name, context = context)


@method_decorator(staff_member_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class ManageOrdersView(View):
    template_name  =  'siteadmin/orders.html'
 

    def get(self, request):
        order_data = OrderDetailModel.objects.all()
        context =  {
            'order_data': order_data,
        }    
        return render(request, self.template_name, context=context)
    




@method_decorator(staff_member_required(login_url='/auth/login', redirect_field_name='ReturnUrl'), name='dispatch' )
class EditOrderView(View):
    form_model  =  OrderDetailsFormAdminSide
    model  = OrderDetailModel 
    template_name = 'siteadmin/addform.html'


    def get(self, request, order_id ):
        if order_id is not None:
            order_instance   =  get_object_or_404(self.model, id =  order_id)
            order_form  =  self.form_model(instance =  order_instance)
        else:
            order_form =  self.form_model()

        context = {
            'form_title': 'Manage Inventory', 
            'form': order_form, 
        }
        return render(request, self.template_name, context=   context)



    def post(self, request, order_id):
        
        order_instance  = get_object_or_404(self.model, id  = order_id)
        order_form =  self.form_model(request.POST  , request.FILES, instance  = order_instance)    

        context = {
            'form_title': 'Manage Orders', 
            'form': order_form, 
        }

        if order_form.is_valid():
            order_form.save(context  =  request)
            return redirect('manage_order')
        
        return render(request, self.template_name, context=context)