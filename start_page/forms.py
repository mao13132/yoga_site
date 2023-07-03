from django import forms
from orders.models import Orders

class OneFormOrders(forms.Form):
    offer = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'pattern': '\+{0,1}[0-9]+',
                                                                         'class': 'form-control'}), required=True)
    telegram = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    price = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    comments = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    buy_chat = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    source = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
