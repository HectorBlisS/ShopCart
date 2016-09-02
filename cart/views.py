from django.shortcuts import render, get_object_or_404, redirect
from .forms import CartAddProductForm
from django.views.generic import View
from .cart import Cart
from shop.models import Product


class Agregar(View):
	def post(self,request,product_id):
		cart = Cart(request)
		product = get_object_or_404(Product,id=product_id)
		form = CartAddProductForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			cart.add(product=product,
				quantity=cd['quantity'],
				update_quantity=cd['update'])
		return redirect('cart:cart_detail')

class Remove(View):
	def post(self,request,product_id):
		cart = Cart(request)
		product = get_object_or_404(Product,id=product_id)
		cart.remove(product)
		return redirect('cart:cart_detail')

class Detalle(View):
	def get(self,request):
		cart = Cart(request)
		return render(request,'cart/detalle.html',{'cart':cart})












