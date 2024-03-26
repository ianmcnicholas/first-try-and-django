from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request,
                  "index.html",
                  {"list_of_products": products}
                  )


def new(request):
    return HttpResponse("New Products")
