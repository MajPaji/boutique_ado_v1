from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categries = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categries]

        self.fields['category'].choices = friendly_name

        for field_name, field in self.fields.items():
            field.widget.attr['class'] = 'border-black rounded-0'
