from django.shortcuts import render
from .forms import PizzaForms
# Create your views here.

def home(request):
    return render(request,'pizza/home.html')


def order(request):

    if request.method=='POST':
        filled_form=PizzaForms(request.POST)
        if filled_form.is_valid():
            note='Thanks for ordering! Your %s %s  and %s pizza is on its way !'%(filled_form.cleaned_data['size'],
                                                                                  filled_form.cleaned_data['topping1'],
                                                                                  filled_form.cleaned_data['topping2'],)
            new_form=PizzaForms()
            return render(request,'pizza/order.html',{'pizzaform':new_form,'note':note})
    else:

        form=PizzaForms()
        return render(request,'pizza/order.html',{'pizzaform':form})