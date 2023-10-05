from typing import Iterable, Optional
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify

from authentication.models import User

# Create your models here.


class ProductCategoryModel(models.Model):
    id  =  models.BigAutoField(primary_key=True)
    category_name =   models.CharField(max_length=50, null=False, blank=False, db_column='category_name')
    category_url_name =  models.CharField(max_length=50, db_column='category_url_name', null=True, blank=True)
    is_active  =   models.BooleanField(default=True, db_column='is_active')
    created_on  =  models.DateTimeField(auto_now_add=True, db_column='created_on')

    def save(self, *args, **kwargs):
        if not self.category_url_name:
            self.category_url_name  =  slugify(f'{self.category_name}')
        return super().save(*args, **kwargs)


    def __str__(self):
        return self.category_name



    class Meta:
        db_table  =  'product_category'



class ProductModel(models.Model):

    
    id  =  models.BigAutoField(primary_key=True)
    product_name  =  models.CharField(max_length=200, null=False, blank=False, db_column='product_name')
    product_description  = models.TextField(_("description"), db_column  = 'product_description')
    categories = models.ManyToManyField(ProductCategoryModel, db_column='categories', related_name='products')
    manufactured_date  = models.DateField(auto_now_add=True, db_column='manufactured_date')
    is_active  =  models.BooleanField(_("Active"), default=True, db_column='is_active')
    price  =  models.DecimalField(null=False, blank=False, db_column='price', decimal_places=3, max_digits=10)
    slug = models.SlugField(db_column='slug',  null=True, blank=True, max_length=200, unique=True)
    created_on  =  models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):  # new
        if self.slug == '' or self.slug is None:
            self.slug = slugify(f'{self.product_name}')
        return super().save(*args, **kwargs)


    class Meta:
        db_table  =   'product'



class ProductImageModel(models.Model):
    def product_img_path(self, filename):
        return '{2}/{1}'.format(self.id, filename, 'Products')

    id = models.BigAutoField(primary_key=True)
    product_id =  models.ForeignKey(ProductModel, null=False, blank=False, on_delete=models.CASCADE,  db_column='product_id', related_name='images')
    images =  models.ImageField(_("Display Picture"), upload_to=product_img_path,  db_column='images', null=False, blank=False)

    class Meta:
        db_table = 'product_images'
    
    def __str__(self) -> str:
        return f"Images of {self.product_id.product_name}"
    



class InventoryModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id   =  models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING, db_column='product_id')
    quantity  =  models.IntegerField(null=False, blank=False, db_column='quantity')
    rate   =  models.DecimalField(null=False, blank=False, db_column='rate',decimal_places=3, max_digits=10 )
    amount =  models.DecimalField(decimal_places=3, max_digits=10, null=True, blank=True)
    created_by  =  models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)

    class Meta:
        db_table =  'inventory'

    def save(self, *args, **kwargs):
        if not self.amount:
            self.amount  =  self.quantity * self.rate
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.product_id.product_name



class OrderDetailModel(models.Model):

    ORDER_STATUS = (
    ("CONFIRMED", "CONFIRMED"),
    ("DISPTACHED", "DISPTACHED"),
    ("DELIVERED", "DELIVERED"),
    ("CANCELLED", "CANCELLED")
    )

    id  = models.BigAutoField(primary_key=True)
    order_uuid  =  models.UUIDField(default=uuid.uuid4, editable=False, null=False , blank=False)
    ordered_by =  models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='ordered_by')
    product_id  =  models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING, db_column='product_id')
    quantity  =  models.PositiveIntegerField(null=False, blank=False, db_column='quantity')
    total_price  =  models.DecimalField(decimal_places=3, max_digits=10, db_column='total_price')
    customer_name = models.CharField(_("Customer Name"), max_length=50, null=False, blank=False)
    primary_delivery_address  =  models.CharField(max_length=100, blank=False, null=False )
    contact_number =   models.CharField(max_length=20, null=False, blank=False)
    secondary_delivery_address  =  models.CharField(max_length=100, null=True, blank=True)
    postal_code  =  models.CharField(max_length=20, null=False, blank=False)
    city  =  models.CharField(max_length=40, null=False, blank=False)
    ordered_date   = models.DateField(auto_now_add=True)
    order_status  =  models.CharField(max_length=20, choices=ORDER_STATUS, default='CONFIRMED')
    payment_completed =  models.BooleanField(default=False)



    class Meta:
        db_table  = 'order_details'
    
    

    def __str__(self):
        return self.customer_name
    