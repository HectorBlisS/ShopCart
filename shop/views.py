from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Product
from cart.forms import CartAddProductForm


class Lista(View):
	def get(self, request):
		productos = Product.objects.all()
		template_name = 'shop/lista.html'
		context = {
		'productos':productos
		}
		return render(request,template_name,context)

class Detalle(View):
	def get(self, request, product_id):
		template_name = 'shop/detalle.html'
		producto = get_object_or_404(Product,id=product_id)
		form = CartAddProductForm()
		context = {
		'producto':producto,
		'form':form
		}
		return render(request,template_name,context)

