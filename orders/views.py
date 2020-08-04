from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Menu,Shopping_Cart,Topping,Order_Items,Order,Addition
# Create your views here.

def login_view(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(request,username = username,password=password)
	if user is None:
		return render(request,"orders/login.html")
	login(request,user)
	return HttpResponseRedirect(reverse('index'))

def register(request):
	return render(request,'orders/register.html')

def registered(request):
	username = request.POST["username"]
	password = request.POST["password"]
	email = request.POST["email"]
	first_name = request.POST["first_name"]
	user =  User.objects.create_user(username,email,password)
	user.first_name = first_name
	user.save()
	return HttpResponse("register")

def logout_view(request):
	logout(request)
	return render(request,"orders/login.html")

def index(request):
	if not request.user.is_authenticated:
		return render(request,"orders/login.html")
	orders = Shopping_Cart.objects.filter(user = request.user)
	total = 0
	for order in orders:
		total = order.menu.cost + total
		for addition in order.addition.all():
			total = addition.cost + total
	context = {
	'item_cart': orders,
	'total':total
	}
	return render(request, "orders/index.html",context)

def page(request,page_id):
	if page_id is 1:
		orders = Shopping_Cart.objects.filter(user = request.user)
		toppings = Topping.objects.all();
		menu = Menu.objects.filter(category = "Regular Pizza")
		context = {
		"toppings":toppings,
		"orders":orders,
		"menu":menu
		}
		return render(request,"orders/reg_pizza.html",context)
	elif page_id is 2:
		orders = Shopping_Cart.objects.filter(user = request.user)
		toppings = Topping.objects.all();
		menu = Menu.objects.filter(category = "Sicilian Pizza")
		context = {
		"toppings":toppings,
		"orders":orders,
		"menu":menu
		}
		return render(request,"orders/sic_pizza.html",context)
	elif page_id is 3:
		orders = Shopping_Cart.objects.filter(user = request.user)
		addition = Addition.objects.all();
		menu = Menu.objects.filter(category = "Subs")
		context = {
		"additions":addition,
		"orders":orders,
		"menu":menu
		}
		return render(request,"orders/subs.html",context)
	elif page_id is 4:
		orders = Shopping_Cart.objects.filter(user = request.user)
		menu = Menu.objects.filter(category = "Pasta")
		context = {
		"orders":orders,
		"menu":menu
		}
		return render(request,"orders/pasta.html",context)
	elif page_id is 5:
		orders = Shopping_Cart.objects.filter(user = request.user)
		menu = Menu.objects.filter(category = "Salad")
		context = {
		"orders":orders,
		"menu":menu
		}
		return render(request,"orders/pasta.html",context)
	elif page_id is 6:
		orders = Shopping_Cart.objects.filter(user = request.user)
		menu = Menu.objects.filter(category = "Dinner Platter")
		context = {
		"orders":orders,
		"menu":menu
		}
		return render(request,"orders/dinner.html",context)

def added_cart(request):
	print(request.POST['menu_item'])
	menu_item = Menu.objects.get(pk = request.POST['menu_item'])
	toppings = request.POST.getlist('topping')
	additions = request.POST.getlist('addition')
	f = Shopping_Cart(user = request.user,menu = menu_item,quantity = 1)
	f.save()
	for topping in toppings:
		top = Topping.objects.get(pk = topping)
		f.topping.add(top)
	for addition in additions:
		adds = Addition.objects.get(pk = addition)
		f.addition.add(adds)
	return HttpResponseRedirect(reverse('index'))

def place(request):
	user = request.user
	items_todo = Shopping_Cart.objects.filter(user = user)
	order = Order(placed_by = user,total = 0)
	order.save()
	for item in items_todo:
		f = Order_Items(order = order, menu = item.menu, quantity = 1)
		f.save()
		for top in item.topping.all():
			f.topping.add(top)
		for adds in item.addition.all():
			order.total = order.total + adds.cost
			f.addition.add(adds)
		# print(item.menu.cost)
		order.total = order.total + item.menu.cost
		item.delete()
	order.save()
	return HttpResponseRedirect(reverse('index'))		

def orders(request):
	if not request.user.is_authenticated:
		return render(request,"orders/login.html")
	elif not request.user.is_staff:
		return render(request,"orders/login.html")
	orders = Order.objects.all()
	context = {
		'orders':orders
	}
	return render(request,'orders/orders.html',context)

def confirm(request):
	orders = Shopping_Cart.objects.filter(user = request.user)
	total = 0
	for order in orders:
		total = order.menu.cost + total
		for addition in order.addition.all():
			total = addition.cost + total
	context = {
	'item_cart': orders,
	'total':total
	}
	return render(request,'orders/confirm.html',context)

def previous_orders(request):
	user = request.user;
	orders = Order.objects.filter(placed_by = user)
	context = {
		'orders':orders
	}
	return render(request,'orders/previous.html',context)