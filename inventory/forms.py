from django import forms


class CreateForm(forms.Form):
    product_id = forms.CharField(label="Product ID", max_length=100)
