from django.shortcuts import render
from .forms import PizzaForms
# Create your views here.

def home(request):
    return render(request,'pizza/home.html')


def order(request):
    form=PizzaForms()
    return render(request,'pizza/order.html',{'pizzaform':form})