from django import forms
from .models import BannerImagesModel


class BannerImageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40'
    

    class Meta:
        model =  BannerImagesModel
        fields = '__all__'