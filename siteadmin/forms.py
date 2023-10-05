
from product.models import OrderDetailModel
from django import forms


class OrderDetailsFormAdminSide(forms.ModelForm):
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40 cursor-not-allowed'
            if visible.name in ('payment_completed', 'order_status' ):
                visible.field.widget.attrs['disabled'] = False
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40 cursor-pointer'


            else:
                visible.field.widget.attrs['disabled'] = True
               




    class Meta:
        model  =  OrderDetailModel
        fields=  '__all__'
