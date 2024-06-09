from django import forms
from .models import Pizza,Size


# class PizzaForms(forms.Form):

#     topping1=forms.CharField(label='Topping1',max_length=100)
#     topping2=forms.CharField(label='Topping2',max_length=100)
#     size=forms.ChoiceField(label='Size',choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])

class PizzaForms(forms.ModelForm):

    size=forms.ModelChoiceField(queryset=Size.objects,empty_label=None,widget=forms.RadioSelect)

    class Meta:
        model=Pizza
        fields=['topping1','topping2','size']
        labels={'topping1':'Topping 1','topping2':'Topping 2','size':'Size'}
        