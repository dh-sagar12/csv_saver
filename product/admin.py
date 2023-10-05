from django.contrib import admin
from .models import  *

# Register your models here.
admin.site.register(ProductCategoryModel)
admin.site.register(ProductImageModel)
admin.site.register(ProductModel)
admin.site.register(InventoryModel)
admin.site.register(OrderDetailModel)