
from django import forms
from Home.models import Product, Product_images


class Product_form(forms.ModelForm):
    titel = forms.CharField(widget=forms.TextInput(attrs={
                            'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'}))
    category = forms.Select()
    price = forms.DecimalField(widget=forms.NumberInput(
        attrs={'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'}))
    stockag = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-textarea focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
               'rows': '5'}))
    meta_titel = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray form-input',
               'placeholder': 'typing like this : Product name  ,other product name '}))
    meta_description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-textarea focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
               'rows': '3',
               'placeholder': 'typing like this : Description , category name colors , sizes ,other product name'}))

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['date_created', 'slug']


class Product_images_form(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'multiple': True, }))

    class Meta:
        model = Product_images
        fields = '__all__'
        exclude = ['prod', 'slug']
