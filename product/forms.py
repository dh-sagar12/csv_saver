from typing import Any
from django import forms

from product.models import InventoryModel, OrderDetailModel, ProductCategoryModel, ProductImageModel, ProductModel
from django.forms import inlineformset_factory


class CustomManyToManyFormField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, category):
         return "%s" % category.category_name

        
class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40'
    
    
    class Meta:
        model =  ProductModel
        fields = '__all__'
        

    categories =  CustomManyToManyFormField(
        queryset=ProductCategoryModel.objects.filter(is_active  =  True), 
        widget=forms.CheckboxSelectMultiple

    )

        
class ProductImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40'
                # self.fields['images'].widget = forms.FileInput(attrs={'accept': 'image/*'})
    class Meta:
        model =  ProductImageModel
        fields =('images', )




ProductImageFormSet = inlineformset_factory(ProductModel, ProductImageModel, form=ProductImageForm, extra=1)




class ProductCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40'
    
    class Meta:
        model = ProductCategoryModel
        fields = ("category_name", "category_url_name" ,  "is_active")


class InventoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40'
    
    class Meta:
        model = InventoryModel
        fields = ("product_id", "quantity" ,  "rate", 'amount')

    def save(self, *args, **kwargs) -> Any:
        inventory  =  super().save(commit=False)
        request =  kwargs.get('context')
        inventory.created_by  =  request.user
        inventory.save()
        return inventory




class OrderDetailForm(forms.ModelForm):
     
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40 w-full'


    class Meta:
        model  =  OrderDetailModel
        fields  =  ('quantity',  'customer_name', 'contact_number',  'primary_delivery_address', 'secondary_delivery_address', 'postal_code', 'city'
        )
        widgets= {
            'customer_name': forms.TextInput(attrs= {'placeholder': 'Enter Your Name'}),
            'contact_number': forms.TextInput(attrs= {'placeholder': 'Enter Your Contact Number'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Order Quantity'} ),
            'primary_delivery_address': forms.TextInput(attrs={'placeholder': 'Address Line 1'} ),
            'secondary_delivery_address': forms.TextInput(attrs={'placeholder': 'Address Line 2'} ),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Postal Code'} ),
            'city': forms.TextInput(attrs={'placeholder': 'City'} )
        }

