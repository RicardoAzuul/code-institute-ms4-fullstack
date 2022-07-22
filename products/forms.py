from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Product_Category


class ProductForm(forms.ModelForm):
    """
    Creates a form to add or edit products in the webapp itself
    """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Product_Category.objects.all()
        friendly_names = [(c.id, c.friendly_name2) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
