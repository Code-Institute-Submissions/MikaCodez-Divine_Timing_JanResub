from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductComment


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductCommentForm(forms.ModelForm):
    """ Creates ProductCommentForm class """

    class Meta:
        """ Update Class Meta Data """
        model = ProductComment
        fields = [
            'product_comment',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'product_comment': 'Leave your comment here',
        }
        self.fields['product_comment'].widget.attrs['autofocus'] = True
        self.fields['product_comment'].label = ""
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder