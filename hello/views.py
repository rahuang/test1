from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Test
from .models import ShoppingCart

import requests

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python Test1!')

def main(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def details(request):
    return render(request, 'details.html')

def login(request):
    return render(request, 'login.html')

def products(request):
    return render(request, 'products.html')

def register(request):
    return render(request, 'register.html')

def cart(request):
    cart = ShoppingCart(pic="pic1.jpg", name="Even & Odd", price="$145.99")
    cart.save()
    cart = ShoppingCart(pic="pic2.jpg", name="Buffalo Decollete", price="$185.99")
    cart.save()
    cart = ShoppingCart(pic="pic3.jpg", name="Even & Odd", price="$145.99")
    cart.save()

    return render(request, 'cart.html', {"range": range(3)})

def test(request):
    test = Test(name="hello")
    test.save()

    test = Test.objects.all()
    return render(request, 'db.html', {'greetings': test})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

