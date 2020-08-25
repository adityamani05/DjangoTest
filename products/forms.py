from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "class": "new-class-name two",
            "id": "id-for-text-area",
            "rows": 20,
            "cols": 120,
        }
    ))
    price = forms.DecimalField()
    email = forms.EmailField()

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "abc" in title:
            raise forms.ValidationError("This is not valid title")
        return title
        
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('.com'):
            raise forms.ValidationError("This is not valid email")
        return email


class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "class": "new-class-name two",
            "id": "id-for-text-area",
            "rows": 20,
            "cols": 120,
        }
    ))
    price = forms.DecimalField()
