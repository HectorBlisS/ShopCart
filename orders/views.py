from django.shortcuts import render
from django.views.generic import View
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import OrderItem, Order

class CrearOrden(View):
	def get(self,request):
		form = OrderCreateForm()
		template_name = 'orders/create.html'
		context = {
		'form':form,
		'cart':Cart(request)
		}
		return render(request,template_name,context)

	def post(self, request):
		cart = Cart(request)
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				OrderItem.objects.create(
					order=order,
					product=item['product'],
					price=item['price'],
					quantity=item['quantity']
					)
			#Borramos el carrito
			cart.clear()
			template_name = 'orders/gracias.html'
			context = {
			'order':order
			}
			return render(request,template_name,context)




